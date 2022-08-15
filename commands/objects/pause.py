
class PauseCommand:
    async def execute(self, ctx):
        ctx.voice_client.pause()

