from youtube_transcript_api import YouTubeTranscriptApi
import openai

def getTranscript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript
