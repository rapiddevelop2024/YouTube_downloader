#A function that you can download youtube links  by it
#author : m.dehghan


#install new libraries
pip install pytube

#import needed libraries
import pytube

#function definition
def yt_dl(link):
    yt = pytube.YouTube(link)
    yt.streams.first().download()
    print('downloaded ',link)
	
	
#how to call function

yt_dl('your_youtube_link')
