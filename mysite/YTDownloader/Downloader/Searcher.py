import urllib.request
import re
import json
from django.http import JsonResponse


def YoutubeSearcher(searchString):
    videoUrlTemplate = "https://www.youtube.com/watch?v="
    video_urls = []
    videoThumbs = []

    searchquery = "https://www.youtube.com/results?search_query=" + searchString

    html = urllib.request.urlopen(searchquery)
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    for x in video_id:
        video_urls.append(videoUrlTemplate + x)
        videoThumbs.append("https://i.ytimg.com/vi/" + x + "/sd1.jpg")

    result = {
        'videoUrls': video_urls,
        'videoThumbs': videoThumbs,
    }
    print("******************")
    return JsonResponse(result)

