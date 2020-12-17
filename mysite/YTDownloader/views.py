from django.shortcuts import render
from django.http import HttpRequest
from .Downloader.downloader import video_downloader

# Create your views here.


def youtube_downloader(url):
    url = "https://www.youtube.com/watch?v=FxzYifHV1-A"
    return video_downloader(url)
