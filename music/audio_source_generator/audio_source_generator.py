import discord

from music.audio_source_generator.wrong_link_exception import WrongLinkException
from music.audio_url_retriever import AudioUrlRetriever, WrongUrlException
from music.ffmpeg_handler import FFmpegHandler

class AudioSourceGenerator:
    def __init__(self):
        self.urlRetriever = AudioUrlRetriever()
        self.ffmpegHandler = FFmpegHandler()

    def generate_from_link(self, link):
        try:
            return self.try_to_generate_from_link(link)
        except WrongUrlException:
            raise WrongLinkException()

    def try_to_generate_from_link(self, link):
        url = self.urlRetriever.retrieve_from_link(link)
        source = self.ffmpegHandler.create_audio_from_url(url)

        return source


