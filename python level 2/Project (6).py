from pytube import YouTube


link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

ys = yt.streams
for i in ys:
    print(i)

x =int(input("enter"))
print("Downloading...")
ys[x].download()
print("Download completed!!")
