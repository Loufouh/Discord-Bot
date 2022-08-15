from dummies.voice_client import VoiceClient_dummy

class Channel_dummy:
    def __init__(self, ctx):
        self.ctx = ctx
        self._isConnected = False

    async def connect(self):
        self._isConnected = True
        self.ctx.voice_client = VoiceClient_dummy(self.ctx)

