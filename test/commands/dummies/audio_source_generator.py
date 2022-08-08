import discord

from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy
from test.commands.dummies.ffmpeg_handler import FFmpegHandler_dummy

class AudioSourceGenerator_dummy:
    def __init__(self):
        self.urlRetriever = AudioUrlRetriever_dummy()
        self.ffmpegHandler = FFmpegHandler_dummy()

    def generate_from_link(self, link):
        return discord.AudioSource()

