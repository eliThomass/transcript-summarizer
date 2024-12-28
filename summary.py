from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

# Enter your OWN OpenAI API Key in the string below
client = OpenAI(api_key = '')


def getTranscript(video_id):
    json_transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ''
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
            {"role": "assistant", "content": "Write a 100 word summary of this video"},
            {"role": "user", "content": transcript}
        ]
    )

    summary = response.choices[0].message.content

    return summary
