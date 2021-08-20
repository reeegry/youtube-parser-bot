import urllib.request
import json
import requests
from data.config import *


def youtube_get_information(channel_id):
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


def twitch_get_information(channel_name):
    URL = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'
    auth_url = 'https://id.twitch.tv/oauth2/token'
    aut_params = {'client_id': CLIENT_ID,
                'client_secret': SECRET,
                'grant_type': 'client_credentials'
                }

    aut_call = requests.post(url=auth_url, params=aut_params) 
    access_token = aut_call.json()['access_token']

    head = {
        'Client-ID' : CLIENT_ID,
        'Authorization' :  "Bearer " + access_token
    }

    r = requests.get(URL, headers = head).json()['data']
    if r:
        if r[0]['type'] == 'live':
            return True
    return False




