from Bot import get_bot

class NotConnectedException(Exception):
    pass

@get_bot().command(name='leave')
async def _leave(ctx):
    try:
        await _try_to_leave(ctx)
    except NotConnectedException:
        await ctx.send('Chuis pas connecté %s' % ctx.author.mention)
    
async def _try_to_leave(ctx):
    if ctx.voice_client is None:
        raise NotConnectedException()

    await ctx.send('bye ! %s' % ctx.author.mention)
    await ctx.voice_client.disconnect()

