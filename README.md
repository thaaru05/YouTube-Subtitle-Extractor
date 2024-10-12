# YouTube-Subtitle-Extractor

# YouTube Subtitle Extractor

## Overview

**YouTube Subtitle Extractor** is a Python-based command-line tool designed to extract subtitles (transcripts) from YouTube videos. By leveraging the **`pytube`** library for video data and the **`youtube-transcript-api`** for fetching subtitles, this project provides users with an efficient way to access video transcripts for personal or academic use.

## Features

- **Easy to Use**: A simple command-line interface that requires minimal input.
- **Versatile**: Works with any public YouTube video that has available transcripts.
- **File Output**: Saves subtitles in a clean and readable text file format.

## Installation

To use the YouTube Subtitle Extractor, you need to install the required libraries. Follow the steps below:

1. **Clone the repository or download the script**:
   ```bash
   git clone https://github.com/your_username/youtube-subtitle-extractor.git
   cd youtube-subtitle-extractor


2. **Install the necessary libraries**:
   Use pip to install the required libraries:
   ```bash
   pip install pytube youtube-transcript-api pandas
   ```

## Usage

Once the installation is complete, you can run the YouTube Subtitle Extractor script.

### Functionality

The main functionality of the script is encapsulated in the `get_youtube_subtitles(video_url)` function, which performs the following steps:

1. **Extracts the Video ID**: The function takes a YouTube video URL as input and extracts the video ID.
2. **Fetches the Transcript**: It uses the `youtube-transcript-api` to fetch the available subtitles for the video.
3. **Creates a DataFrame**: The fetched subtitles are organized into a pandas DataFrame for easier handling.
4. **Saves Subtitles to a File**: The subtitles are written to a text file, with each line formatted to show the start time, end time, and text.

## Error Handling

The script includes basic error handling. If an error occurs (for example, if the video has no available subtitles or the URL is invalid), the function will print an error message to the console. Users can enhance this feature by implementing more specific error handling for different scenarios (e.g., network issues, video ID extraction failures).

## Contributing

Contributions are welcome! If you would like to enhance the project, please follow these steps:

1. **Fork the repository**.
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature/AmazingFeature`).
5. **Open a pull request**.

Please ensure your code adheres to the existing code style and includes appropriate tests.
```

### Instructions for Use:
- Replace `your_username` in the clone URL with your actual GitHub username.
- You can add any additional information or sections that might be relevant to your project.

This README format provides a clear overview of the project, its features, and instructions for installation, usage, and contributing, making it suitable for GitHub.
