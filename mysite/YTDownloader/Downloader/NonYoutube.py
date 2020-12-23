import youtube_dl
import time
from django.http import JsonResponse


def NonYoutubeSites(url):
    video_url = url
    video_audio_streams = []

    ydl = youtube_dl.YoutubeDL({"outtmpl": "%(id)s.%(ext)s"})

    with ydl:
        result = ydl.extract_info(
            video_url,
            download=False,  # We just want to extract the info
        )

    video_audio_streams = result
    return JsonResponse(video_audio_streams)
