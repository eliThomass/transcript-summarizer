# transcript-summarizer
A simple project utilizing APIs which gives a summary of a YouTube video using its URL.

To install the required APIs (Python), run these commands into the terminal:
```
pip install youtube-transcript-api
pip install openai
```

Then paste your **OpenAI API** key into the top of the ***summary.py*** file (as seen below)
```python3
# Enter your OWN OpenAI API Key in the string below
client = OpenAI(api_key = ' ENTER KEY HERE ')
```

Then run the program with ```python3 -m main``` and paste your URL as requested, be sure to paste the entire URL.

The program will then return a 100-word summary of the provided video.
