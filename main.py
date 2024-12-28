import summary

video_url = input('Enter video URL: ')
video_id = video_url.replace('https://www.youtube.com/watch?v=', '')

print('--- SUMMARY --- \n')
print(summary.getSummary(video_id))
print('\n')
