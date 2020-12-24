import youtube_dl
import time
from django.http import JsonResponse
from fake_useragent import UserAgent
from .RandomProxy import generateRandomProxy


def NonYoutubeSites(url):
    video_url = url
    video_audio_streams = []

    # get random fake user agent
    ua = UserAgent()

    # get faket proxy
    proxy = generateRandomProxy()

    ydl_opts = {
        "outtmpl": "%(id)s.%(ext)s",
        "--cookies": "/cookies.txt",
        "--user-agent": ua,
        "--proxy": proxy['ip'],
    }
    
    print(proxy['ip'])

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with ydl:
        result = ydl.extract_info(
            video_url,
            download=False,  # We just want to extract the info
        )

    video_audio_streams = result
    return JsonResponse(video_audio_streams)
