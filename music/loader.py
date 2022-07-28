import discord

from music.downloader import get_downloader

class Loader:
    downloader = get_downloader()

    def load_from_link(self, link):
        filename = self.downloader.download_from_link(link)

        return discord.FFmpegPCMAudio(filename)

loader = None

def get_loader():
    global loader

    if loader is None:
        loader = Loader()

    return loader

