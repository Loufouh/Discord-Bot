from Bot import get_bot

@get_bot().command(name='stop')
async def _stop(ctx):
    ctx.voice_client.stop()

