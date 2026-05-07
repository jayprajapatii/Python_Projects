from pytube import YouTube

link = YouTube("https://youtu.be/t10sQb0Zmjs?si=FNeqYICBT6MkWqy2")

video = link.streams.filter(only_audio=True).first()

video.download("D:/python")
