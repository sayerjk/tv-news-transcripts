import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


def get_transcript(address: str) -> dict:
    """Stores features in dictionary. Prep for MongoDB transfer."""

    webpage = 'https://transcripts.cnn.com' + address
    contents = requests.get(webpage)

    soup = BeautifulSoup(contents.text, 'html.parser')
    title = soup.find(attrs='cnnTransStoryHead').text

    cnnBodyText = soup.find_all(name='p', attrs='cnnBodyText')
    cnnBodyText = [attribute.text for attribute in cnnBodyText]
    date = cnnBodyText[0]
    mainBody = cnnBodyText[2]

    mainBody = TextBlob(mainBody)
    positive_polarities = [(i.polarity, i) for i in mainBody.sentences if i.polarity > 0]
    negative_polarities = [(i.polarity, i) for i in mainBody.sentences if i.polarity <= 0]
    sentence_breakdown = [positive_polarities, negative_polarities]
    ratio = len(positive_polarities) / (len(positive_polarities) + len(negative_polarities))

    # TODO - engineer `common_phrases` field (NLTK bigrams and trigrams?)
    results = {
        'title': title,
        'date': date,
        'polarity': mainBody.polarity,
        'subjectivity': mainBody.subjectivity,
        # TODO - fix Sentence() datatype here
        # 'sentence_breakdown': sentence_breakdown,
        'percent_over_zero': ratio,
        'network': webpage
    }

    return results


def get_transcript_links(webpage: str) -> list[str]:
    """Provides 100 most recent links to transcripts for a given CNN show"""
    index_contents = requests.get(webpage)
    index_soup = BeautifulSoup(index_contents.text, 'html.parser')
    transcript_links = []
    for i in index_soup.find_all(name='a'):
        if i.get('href'):
            if i.get('href')[0:5] == '/show':
                transcript_links.append(i.get('href'))
    return transcript_links


def segment_links(url: str) -> list[str]:
    """
    Return links to all CNN segments with transcripts online from cnn.transcripts.com
    Needs adaptation for other news websites.
    """
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    show_links = []
    for i in soup.find_all(name='a'):
        if i.get('href'):
            if i.get('href')[0:5] == '/show':
                show_links.append((i.get('href'), i.text))

    return show_links

