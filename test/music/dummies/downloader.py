
class Downloader_dummy:
    requestedDownload = False
    lastLink = None

    def download_from_link(self, link):
        self.lastLink = link
        self.requestedDownload = True

        return 'music_files/test.mp3'

    def reset(self):
        self.requestedDownload = False
        self.lastLink = None

downloader = None

def get_downloader():
    global downloader

    if downloader is None:
        downloader = Downloader_dummy()

    return downloader

