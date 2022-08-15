
class StopCommand:
    async def execute(self, ctx):
        ctx.voice_client.stop()

