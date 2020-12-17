import youtube_dl
import time

video_url = "https://www.youtube.com/watch?v=c1ivrVbzUGw"
video_audio_streams = []

ydl = youtube_dl.YoutubeDL({"outtmpl": "%(id)s.%(ext)s"})

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
        file_size = f"{round(file_size / 1000000,2)}"
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


duration = time.strftime("%H:%M:%S", time.gmtime(int(result["duration"])))

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
