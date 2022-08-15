
class ResumeCommand:
    async def execute(self, ctx):
        ctx.voice_client.resume()

