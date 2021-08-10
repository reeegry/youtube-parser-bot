import urllib.request
import json
from data.config import *


def get_information(channel_id):
    api_key = YOUTUBE_API_KEY
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"
    base_video_link = "https://www.youtube.com/watch?v="
    first_url = base_search_url + f"key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    inp = urllib.request.urlopen(first_url)
    resp = json.load(inp)
    for i in resp["items"]:
        print(i)
        if i["id"]["kind"] == "youtube#video":
            video_link = base_video_link + i["id"]["videoId"]
            video_title = i["snippet"]["title"]
            return video_title, video_link


