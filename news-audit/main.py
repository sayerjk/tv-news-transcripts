from transcripts import get_transcript, get_transcript_links, segment_links
from data import send_to_mongo

show_index = 'https://transcripts.cnn.com/show/acd'
batch = [get_transcript(item) for item in get_transcript_links(show_index)[:3]]
# print(f'\nSample entry: {batch[0]}')

front_page = 'https://transcripts.cnn.com/'
idx = segment_links(front_page)
# print(f'All shows: {idx}')

db_name = 'transcripts'
col_name = 'sentiment_textblob'
send_to_mongo(db_name, col_name, batch[0])

print('Done')
