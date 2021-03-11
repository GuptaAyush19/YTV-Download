import os
from pytube import YouTube

class Video:
    def __init__(self, video_url:str, path:str):
        self.video_url = video_url
        self.path = path
        self.yt = YouTube(video_url)
        
    def download(self):
        """Download single youtube video to the specified directory path.
        The highest resolution video will only be downloaded.

        Args:
            video_url (str): YouTube video url
            path (str): Directory path where the mp4 will be downloaded
        """
        #TODO: Add a resolution arguement
        try:
            yt = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        except Exception:
            print(f'Video {self.video_url} is unavaialable, skipping.')
        else:
            print(f"Downloading video: {self.title}")
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        yt.download(self.path)
        
    @property
    def title(self):
        return str(self.yt.title)
    
    @property
    def thumbnail_url(self):
        return str(self.yt.thumbnail_url)