from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .Downloader.downloader import video_downloader
from .Downloader.NonYoutube import NonYoutubeSites
from django.http import JsonResponse
from .Downloader.Searcher import YoutubeSearcher
from ratelimit.decorators import ratelimit

# Create your views here.


@ratelimit(key='ip', rate='15/m', block=True)
def youtube_downloader(request, url=None):

    url = request.GET['url']

    if "youtube.com" in url:

        return video_downloader(url)

    else:
        return NonYoutubeSites(url)


@ratelimit(key='ip', rate='15/m', block=True)
def searcher(request, searchString=None):
    searchString = request.GET['search']

    return YoutubeSearcher(searchString)
