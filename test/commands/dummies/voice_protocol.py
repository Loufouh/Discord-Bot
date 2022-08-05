
class VoiceProtocol_dummy:
    def __init__(self, ctx):
        self.ctx = ctx

    async def disconnect(self):
        await self.ctx.author.voice.channel._disconnect()

