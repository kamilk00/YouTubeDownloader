from pytube import YouTube
import validators

def download(URL, format):

    #download video
    if choice == '1':

        youTubeVideo = YouTube(URL, use_oauth = True, allow_oauth_cache = True)
        youTubeVideo = youTubeVideo.streams.get_highest_resolution()
        try:
            youTubeVideo.download()
            print("Download is completed successfully")
        except:
            print("An error has occurred")
    
    #download only audio
    elif choice == '2':

        youTubeAudio = YouTube(URL, use_oauth = True, allow_oauth_cache = True)
        youTubeAudio = youTubeAudio.streams.filter(only_audio = True).first()
        try:
            youTubeAudio.download()
            print("Download is completed successfully")
        except:
            print("An error has occurred")

    #incorrect choice
    else:
        print("Incorrect choice!")


youTube_URL = input("Paste your youtube URL:\n")
choice = input("Choose format: \n1. Video\n2. Audio \n")

if "youtube.com" in youTube_URL and validators.url(youTube_URL):
    download(youTube_URL, choice)

else:
    print("Incorrect URL!")