from Bot import get_bot

@get_bot().command(name='pause')
async def _pause(ctx):
    ctx.voice_client.pause()

