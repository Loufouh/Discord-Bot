from Bot import get_bot

from discord.errors import ClientException
from commands.exceptions.exceptions import AuthorNotConnectedException, AlreadyConnectedException

@get_bot().command(name='join')
async def _join(ctx):
    try:
        await _try_to_join(ctx)
    except AuthorNotConnectedException:
        await ctx.send('Je trouve pas ton salon audio %s' % ctx.author.mention)
    except AlreadyConnectedException:
        await ctx.send('Je suis déjà connecté %s' % ctx.author.mention)

async def _try_to_join(ctx):
    if ctx.author.voice is None:
        raise AuthorNotConnectedException()
    elif ctx.voice_client is not None:
        raise AlreadyConnectedException()

    await ctx.send('J\'arrive %s !' % ctx.author.mention)
    await ctx.author.voice.channel.connect()

