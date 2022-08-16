
class QueuePlayer_dummy:
    def __init__(self):
        self.voiceClient = None

        self._calledNext = False
        self._calledPlay = False

    def play(self, voiceClient):
        self.voiceClient = voiceClient
        self._calledPlay = True

    def next(self):
        self._calledNext = True

