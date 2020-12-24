from django.shortcuts import render
from django.http import HttpRequest
from .Downloader.downloader import video_downloader
from .Downloader.NonYoutube import NonYoutubeSites
from django.http import JsonResponse
from .Downloader.Searcher import YoutubeSearcher

# Create your views here.


def youtube_downloader(request, url=None):

    url = request.GET['url']
    #url = "https://www.reddit.com/r/gifs/comments/kgmsvp/ski_jump_252_meters/"

    if "youtube.com" in url:
        # return video_downloader(url)
        return video_downloader(url)

    else:
        return NonYoutubeSites(url)


def searcher(request, searchString=None):
    searchString = request.GET['search']

    return YoutubeSearcher(searchString)
