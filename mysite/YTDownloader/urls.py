from django.urls import path
from .views import youtube_downloader
from .views import searcher

urlpatterns = [
    path('downloader/', youtube_downloader, name="yt_downloader"),
    path('searcher/', searcher, name="yt_searcher")
]
