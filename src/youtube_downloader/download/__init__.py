from pytube import YouTube
import os

URL = "https://www.youtube.com/watch?v=dut9EnbFym0"

def download_youtube(video_url:str, path:str):
    """Download single youtube video to the specified directory path.
    The highest resolution video will only be downloaded.

    Args:
        video_url (str): YouTube video url
        path (str): Directory path where the mp4 will be downloaded
    """
    #TODO: Add a resolution arguement
    yt = YouTube(video_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
