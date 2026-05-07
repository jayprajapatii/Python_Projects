from pytube import YouTube

url = str(input("enter the youtube video url :"))
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
stream.download("D:/python")
print("Download Complete!")
    



# from pytube import YouTube

# url = 'https://youtu.be/FudfVyYWNxQ?si=Zecd1xbxa6zY3IX3'

# my_video = YouTube(url)

# print(my_video.title)

# my_video.streams.filter(res='720p').first().download()