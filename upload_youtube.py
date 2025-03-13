import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def upload_video(youtube, filename, title, description, tags):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "27",  # Category ID for Education
            },
            "status": {"privacyStatus": "public"},
        },
        media_body=filename,
    )
    request.execute()

youtube = authenticate()
upload_video(youtube, "final_video.mp4", "AI Tech Update", "Latest AI news from Twitter", ["AI", "Tech", "News"])
