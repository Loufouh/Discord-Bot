import discord

from music.audio_source_generator import WrongLinkException

from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy
from test.commands.dummies.ffmpeg_handler import FFmpegHandler_dummy

class AudioSourceGenerator_dummy:
    def __init__(self):
        self.triggerWrongLinkException = False

        self.urlRetriever = AudioUrlRetriever_dummy()
        self.ffmpegHandler = FFmpegHandler_dummy()

    def generate_from_link(self, link):
        if self.triggerWrongLinkException:
            raise WrongLinkException()

        return discord.AudioSource()

