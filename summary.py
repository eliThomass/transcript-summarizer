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
            {"role": "assistant", "content": "Write a 100-word summary of the video." },
            {"role": "user", "content": transcript}
        ]
    )

    summary = response.choices[0].message.content

    return summary

def getTimestamps(video_id):
    transcript = str(YouTubeTranscriptApi.get_transcript(video_id))

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages =   [
            {"role": "system", "content": "You are a database organizer."},
            {"role": "assistant", "content": "data is stroed in JSON {text:'', start:'', duration:''}"},
            {"role": "assistant", "content": transcript},
            {"role": "user", "content": "Give the main topics discussed in the video, along with start time codes in seconds rounded to nearest whole value"}
        ]
    )

    summary = response.choices[0].message.content

    return summary