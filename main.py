import summary

video_url = input('Enter video URL: ')
video_id = video_url.replace('https://www.youtube.com/watch?v=', '')

print('\n--- SUMMARY --- \n')
print(summary.getSummary(video_id))
print('\n')
print('--- TIMESTAMPS --- \n')
print(summary.getTimestamps(video_id))
print('\n')