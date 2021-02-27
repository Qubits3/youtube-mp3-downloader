from __future__ import unicode_literals
import youtube_dl

num_array = ["https://www.youtube.com/watch?v=4dtZ4TvftlU",
             "https://www.youtube.com/watch?v=bmQwZhcZkbU"]

# print("Insert the link")
# link = input("")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/%USERNAME%/Desktop/Music/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(num_array)
