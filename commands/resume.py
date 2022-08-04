from Bot import get_bot

@get_bot().command(name='resume')
async def _resume(ctx):
    ctx.voice_client.resume()
 
