import discord

from music.audio_source_generator.common import WrongLinkException

from dummies.audio_url_retriever import AudioUrlRetriever_dummy
from dummies.ffmpeg_handler import FFmpegHandler_dummy

class AudioSourceGenerator_dummy:
    def __init__(self):
        self.triggerWrongLinkException = False

        self.urlRetriever = AudioUrlRetriever_dummy()
        self.ffmpegHandler = FFmpegHandler_dummy()

    def generate_from_link(self, link):
        if self.triggerWrongLinkException:
            raise WrongLinkException()

        return discord.AudioSource()

