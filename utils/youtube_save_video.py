"""
https://rapidapi.com/ytdlfree/api/youtube-v31/
https://rapidapi.com/ytjar/api/ytstream-download-youtube-videos/
https://rapidapi.com/Glavier/api/youtube138/
https://rapidapi.com/DataFanatic/api/youtube-media-downloader/
"""
# 500 manth
# 50 day
# 550 manth
# 200 manth
import requests

url = "https://youtube-search-and-download.p.rapidapi.com/video"

headers = {
    "X-RapidAPI-Key": "cad619cee0msh8c8313c370d9792p15bdebjsnb5d643e47069",
    "X-RapidAPI-Host": "youtube-search-and-download.p.rapidapi.com"
}


async def youtube_save_video(urls):
    querystring = {"id": urls[17:]}
    response = requests.request("GET", url, headers=headers, params=querystring)
    link = response.json()['streamingData']['formats'][2]['url']
    return link