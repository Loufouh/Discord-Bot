from music import youtube_mp3_download

class Downloader:
    def download_from_link(self, link, testing=False):
        return youtube_mp3_download.download(link, testing=testing)

downloader = None

def get_downloader():
    global downloader

    if downloader is None:
        downloader = Downloader()

    return downloader

