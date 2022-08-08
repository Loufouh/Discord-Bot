from test.commands.dummies.channel import Channel_dummy

class VoiceState_dummy:
    def __init__(self, ctx):
        self.ctx = ctx
        self.channel = Channel_dummy(ctx)

    async def _disconnect(self):
        self.channel.is_connected = False
        self.ctx.voice_client = None

