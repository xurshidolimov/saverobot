"""
https://rapidapi.com/maatootz/api/tiktok-downloader-download-tiktok-videos-without-watermark/
"""
# 1000 manth
import requests

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

headers = {
    "X-RapidAPI-Key": "cad619cee0msh8c8313c370d9792p15bdebjsnb5d643e47069",
    "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
}


async def tik_tok_save_video(urls):
    querystring = {"url": urls}
    response = requests.request("GET", url, headers=headers, params=querystring)
    link = response.json()['video'][0]
    return link