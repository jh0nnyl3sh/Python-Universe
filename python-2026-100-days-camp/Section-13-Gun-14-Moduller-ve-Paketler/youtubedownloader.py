import pytubefix

url = input("Enter the YouTube video URL: ")

path = ""

pytubefix.YouTube(url).streams.get_lowest_resolution().download(output_path=path)

