from test.commands.dummies.voice_protocol import VoiceProtocol_dummy

class Channel_dummy:
    def __init__(self, ctx):
        self.ctx = ctx
        self._isConnected = False

    async def connect(self):
        self._isConnected = True
        self.ctx.voice_client = VoiceProtocol_dummy(self.ctx)

    async def _disconnect(self):
        self._isConnected = False
        self.ctx.voice_client = None

