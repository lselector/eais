
## Plan to transition static website to add/update content automatically.

- Step 1 - create a simple static website

- Step 2 - add email forms to all pages

- Step 3 - upload it to CloudFlare Pages project - and move DNS to it

- Step 4 - test python script to get data from YouTube:
  run locally from my laptop 
  using YouTube Data API + youtube-transcript-api
  to extract metadata of videos in my YT channel 
  (video date, URL, title, description, transcript)

- Step 5 - improve script to extract metadata 
  from specific video or by date range
  and save into individual JSON files 
  (create a separate directory for those files).
  Add option to pull only most recent metadata which was not pulled yet

- Step 6 - write python script using Claude API 
  to generate a nice MD file for each JSON file
  and put them under website/content

  Step 7 - create a build script to populate the website/blog from inventory
  Make blog navigation

  Step 8 - create an upload script to publish the website to CloudFlare


=======================================================

Below is a step-by-step guide to install and test both APIs 

## Install Required Libraries

Open your terminal and run these commands:

```bash
# Install YouTube Data API client library
pip install --upgrade google-api-python-client

# Install authentication libraries for YouTube Data API
pip install --upgrade google-auth-oauthlib google-auth-httplib2

# Install YouTube Transcript API
pip install youtube-transcript-api
```

## Set Up YouTube Data API Credentials

### Create API Key

- Go to [Google Cloud Console](https://console.cloud.google.com/)[1]
- Create a new project or select an existing one
- Navigate to "APIs & Services" → "Library"
- Search for "YouTube Data API v3" and enable it[2][1]
- Go to "APIs & Services" → "Credentials"
- Click "Create Credentials" → "API Key"[2][1]
- Copy your API key and restrict it to YouTube Data API v3 only (recommended)[3]

## Test YouTube Data API

Create a test file `test_youtube_data.py`:

```python
from googleapiclient.discovery import build

# Replace with your API key
API_KEY = 'YOUR_API_KEY_HERE'

# Build the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Get your channel's videos (replace with your channel ID)
request = youtube.search().list(
    part='snippet',
    channelId='YOUR_CHANNEL_ID',  # Find this in your YouTube Studio
    maxResults=5,
    order='date',
    type='video'
)

response = request.execute()

# Print video details
for item in response['items']:
    video_id = item['id']['videoId']
    title = item['snippet']['title']
    published_at = item['snippet']['publishedAt']
    description = item['snippet']['description']
    
    print(f"Video ID: {video_id}")
    print(f"Title: {title}")
    print(f"Published: {published_at}")
    print(f"Description: {description[:100]}...")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    print("-" * 80)
```

Run it:
```bash
python test_youtube_data.py
```

## Test YouTube Transcript API

Create a test file `test_transcript.py`:

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with a video ID from your channel
video_id = 'YOUR_VIDEO_ID'  # e.g., 'dQw4w9WgXcQ'

try:
    # Initialize the API
    ytt_api = YouTubeTranscriptApi()
    
    # Fetch the transcript
    transcript = ytt_api.fetch(video_id)
    
    print(f"Video ID: {video_id}")
    print(f"Language: {transcript.language}")
    print(f"Is Auto-Generated: {transcript.is_generated}")
    print(f"Number of segments: {len(transcript)}")
    print("\nFirst 3 transcript segments:")
    
    for snippet in transcript[:3]:
        print(f"[{snippet.start:.2f}s] {snippet.text}")
    
    # Convert to raw data format
    raw_data = transcript.to_raw_data()
    print(f"\nRaw data sample: {raw_data[0]}")
    
except Exception as e:
    print(f"Error: {e}")
```

Run it:
```bash
python test_transcript.py
```

## Combined Test Script

Create `test_combined.py` to test both APIs together:[4][1]

```python
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

API_KEY = 'YOUR_API_KEY_HERE'
CHANNEL_ID = 'YOUR_CHANNEL_ID_HERE'

# Initialize both APIs
youtube = build('youtube', 'v3', developerKey=API_KEY)
ytt_api = YouTubeTranscriptApi()

# Get one video from your channel
request = youtube.search().list(
    part='snippet',
    channelId=CHANNEL_ID,
    maxResults=1,
    type='video'
)

response = request.execute()

if response['items']:
    item = response['items'][0]
    video_id = item['id']['videoId']
    
    print(f"Video ID: {video_id}")
    print(f"Title: {item['snippet']['title']}")
    print(f"Published: {item['snippet']['publishedAt']}")
    
    # Get transcript
    try:
        transcript = ytt_api.fetch(video_id)
        print(f"\nTranscript available: Yes")
        print(f"Language: {transcript.language}")
        print(f"Segments: {len(transcript)}")
    except Exception as e:
        print(f"\nTranscript error: {e}")
```

Run it:
```bash
python test_combined.py
```

The YouTube Data API handles all metadata (date, URL, title, description), while `youtube-transcript-api` fetches transcripts without requiring any API key. Both libraries work independently and can be combined in your script to extract all the data you need from your 260+ videos.[5][1][4]

[1](https://serpapi.com/youtube-video-transcript)
[2](https://www.getphyllo.com/post/youtube-api-and-api-key-explained-how-to-get-started-in-2025)
[3](https://www.youtube.com/watch?v=GwTcTQxZ9Xw)
[4](https://www.youtube.com/watch?v=PZ9FrP8atW8)
[5](https://www.xugj520.cn/en/archives/youtube-transcript-api-python-guide-2.html)
[6](https://developers.google.com/youtube/v3/quickstart/python)
[7](https://www.youtube.com/watch?v=FLFKWDEvibw)
[8](https://stackoverflow.com/questions/77348275/how-to-persist-youtube-data-api-v3-authentication-with-google-api-python-client)
[9](https://www.youtube.com/watch?v=th5_9woFJmk)
[10](https://developers.google.com/youtube/v3/guides/authentication)
[11](https://pypi.org/project/youtube-transcript-api/)
[12](https://github.com/happycod3r/YouTube-Data-API-v3-Tools)