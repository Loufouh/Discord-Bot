import discord

class QueuePlayer_dummy:
    def __init__(self):
        self.queue = None
        self.voiceClient = None

        self._calledNext = False
        self._calledPlay = False

    def play(self, voiceClient):
        self.voiceClient = voiceClient
        self._calledPlay = True

        self.voiceClient.play(discord.AudioSource())

    def next(self):
        self._calledNext = True

    def set_queue(self, queue):
        self.queue = queue

