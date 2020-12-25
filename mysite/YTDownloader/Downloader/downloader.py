import youtube_dl
import time
from django.http import JsonResponse
from fake_useragent import UserAgent
from .RandomProxy import generateRandomProxy
    


def video_downloader(url):
    """functions gets youtube video url and retun audio and video download links
    Args:
        url (youtube video link): it can be any youtube video url not playlist
    Returns:
    JSON:
    title:"HUMORPUNK 2023 TURKEY"
    creator:null
    upload_date:"20201217"
    streams:[…] #this array have download links etc
    description:"Lorem ipsum dolor sit ament"
    duration:"00:02:46"
    view_count:38515
    like_count:4419
    dislike_count:68
    thumbnails:
        url	"https://i.ytimg.com/vi/FxzYifHV1-A/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAEq53Iw-6reQRUVDfo8u-XKEBDOA"
        height	188
        width	336
    """

    video_url = url
    video_audio_streams = []

    #get random fake user agent
    ua = UserAgent()
    
    #get faket proxy
    proxy = generateRandomProxy()

    ydl_opts = {
        "outtmpl": "%(id)s.%(ext)s",
        "--cookies": "/cookies.txt",
        "--user-agent": ua,
        "--proxy": proxy['ip'],
        "--no-playlist" : True,
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    
    print(proxy['ip'])

    with ydl:
        result = ydl.extract_info(
            video_url,
            download=False,  # We just want to extract the info
        )

    for x in result["formats"]:
        video_height = None
        video_width = None
        file_size = x["filesize"]
        if file_size is not None:
            file_size = f"{round(file_size / 1000000,2)}"  # byte to megabyte
        if x["height"] is not None:
            video_height = x["height"]
        video_width = x["width"]

        video_audio_streams.append(
            {
                "resolutions": {"height": video_height, "width": video_width},
                "extension": x["ext"],
                "file_size": file_size,
                "video_url": x["url"],
            }
        )

        # duration = time.strftime(
        #     "%H:%M:%S", time.gmtime(int(result["duration"])))
        duration = result["duration"]
        final_context = {
            "title": result["title"],
            "creator": result["creator"],
            "upload_date": result["upload_date"],
            "streams": video_audio_streams,
            "description": result["description"],
            "duration": result["duration"],
            "view_count": result["view_count"],
            "like_count": result["like_count"],
            "dislike_count": result["dislike_count"],
            "duration": duration,
            "thumbnails": {
                "url": result["thumbnails"][3]["url"],
                "height": result["thumbnails"][3]["height"],
                "width": result["thumbnails"][3]["width"],
            },
        }

    return JsonResponse(final_context)
