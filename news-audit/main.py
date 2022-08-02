from transcripts import get_transcript, get_transcript_links, segment_links
# from transcripts import create_jsons
from data import send_to_mongo, search_documents

show_index = 'https://transcripts.cnn.com/show/acd'
db = 'transcripts'
col = 'sentiment_textblob'

# try to convert this into an Iterator Object solution
# batch = [send_to_mongo(db, col, get_transcript(item)) for item in get_transcript_links(show_index)]
# print(f'\nSample entry: {batch[0]}')

# create_jsons(batch)

front_page = 'https://transcripts.cnn.com/'
idx = segment_links(front_page)
print(f'All shows: {idx}')
print('Done')

# test query:
# mongo_query = {}
# search_documents(db, col, mongo_query)
