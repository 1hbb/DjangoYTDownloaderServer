from django.shortcuts import render
from django.http import HttpRequest
from .Downloader.downloader import video_downloader
from .Downloader.NonYoutube import NonYoutubeSites
from django.http import JsonResponse

# Create your views here.


def youtube_downloader(request, url=None):

    url = request.GET['url']
    #url = "https://www.reddit.com/r/gifs/comments/kgmsvp/ski_jump_252_meters/"

    if "youtube.com" in url:
        # return video_downloader(url)
        return NonYoutubeSites(url)

    else:
        return NonYoutubeSites(url)
