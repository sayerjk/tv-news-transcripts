from transcripts import get_transcript, get_transcript_links

show_index = 'https://transcripts.cnn.com/show/acd'
batch = [get_transcript(item) for item in get_transcript_links(show_index)[:3]]
print(batch[0])
print('Done')