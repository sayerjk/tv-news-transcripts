from transcripts import get_transcript, get_transcript_links, segment_links, create_jsons
from data import send_to_mongo

show_index = 'https://transcripts.cnn.com/show/acd'
db = 'transcripts'
col = 'sentiment_textblob'

batch = [send_to_mongo(db, col, get_transcript(item)) for item in get_transcript_links(show_index)]
print(f'\nSample entry: {batch[0]}')

# create_jsons(batch)

front_page = 'https://transcripts.cnn.com/'
idx = segment_links(front_page)
print(f'All shows: {idx}')
print('Done')
