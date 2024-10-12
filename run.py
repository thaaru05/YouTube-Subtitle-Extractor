

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd

# Function to get subtitles from a YouTube video link
def get_youtube_subtitles(video_url):
    try:
        # Extract the video ID from the URL
        video_id = video_url.split('v=')[1].split('&')[0]
        
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Create a DataFrame to organize subtitles
        transcript_df = pd.DataFrame(transcript)
        
        # Save subtitles to a text file
        subtitle_file = f"{video_id}_subtitles.txt"
        with open(subtitle_file, 'w', encoding='utf-8') as f:
            for index, row in transcript_df.iterrows():
                f.write(f"{row['start']:.2f} - {row['start'] + row['duration']:.2f}: {row['text']}\n")

        print(f"Subtitles saved to {subtitle_file}")
        
        return subtitle_file
    
    except Exception as e:
        print("Error:", e)

# Input: YouTube video URL
video_url = input("Enter the YouTube video link: ")

# Get subtitles and save them
subtitle_file = get_youtube_subtitles(video_url)

# Download the subtitles file to Colab
from google.colab import files
files.download(subtitle_file)
