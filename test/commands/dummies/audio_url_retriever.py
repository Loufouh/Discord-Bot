import discord

from music.audio_url_retriever import WrongUrlException

class AudioUrlRetriever_dummy:
    def __init__(self):
        self._retrievedLink = ''
        self._triggerWrongUrlException = False

    def retrieve(self, link):
        if self._triggerWrongUrlException:
            raise WrongUrlException()

        return discord.AudioSource()

