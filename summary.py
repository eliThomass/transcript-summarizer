from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

# Enter your OWN OpenAI API Key in the string below
client = OpenAI(api_key = ' ENTER KEY HERE ')


def getTranscript(video_id):
    transcript = ''
    json_transcript = YouTubeTranscriptApi.get_transcript(video_id)
    counter = 0
    for x in json_transcript:
        sentence = x['text']
        transcript += f' {sentence}'
        counter += 1
        if counter > 3:
            transcript += '\n'
            counter = 0
    return transcript

def getSummary(video_id):
    transcript = getTranscript(video_id)

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages =   [
            {"role": "system", "content": "You are a journalist."},
            {"role": "assistant", "content": "What topics are discussed in the video? Provide start time codes in seconds" },
            {"role": "user", "content": transcript}
        ]
    )

    summary = response.choices[0].message.content

    return summary

def getTimestamps(video_id):
    transcript = getTranscript(video_id)

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages =   [
            {"role": "system", "content": "You are a database organizer."},
            {"role": "assistant", "content": "Give timestamps of things talked about in the transcript, the timestamps should be in MM:SS format"},
            {"role": "user", "content": transcript}
        ]
    )

    summary = response.choices[0].message.content

    return summary