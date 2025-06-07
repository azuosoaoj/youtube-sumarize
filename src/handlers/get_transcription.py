from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import re

def get_youtube_transcript(video_url):
    try:
        # Extract video ID from the URL
        video_id = video_url.split("v=")[-1]
        if "&" in video_id:
            video_id = video_id.split("&")[0]

        available_languages = YouTubeTranscriptApi.list_transcripts(video_id)
        if available_languages:
            language = re.search(r'-\s+(\w+)\s+\(".*"\)\[TRANSLATABLE\]', str(available_languages)).group(1)
            print(language)
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        else:
            return "No transcripts available for this video."
        
        return ' '.join([item['text'] for item in transcript]), language
    
    except Exception as e:
        return f"An error occurred: {e}"
