"""
https://rapidapi.com/maatootz/api/instagram-downloader-download-instagram-videos-stories/
"""
import requests

url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

headers = {
    "X-RapidAPI-Key": "cad619cee0msh8c8313c370d9792p15bdebjsnb5d643e47069",
    "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
}


async def instagram_save_video(urls):
    querystring = {"url": urls}
    response = requests.request("GET", url, headers=headers, params=querystring)
    link = response.json()['media']
    if type(link) == list:
        link = response.json()['media'][0]
        return link
    else:
        return link