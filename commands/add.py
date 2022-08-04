import discord

from Bot import get_bot

from music.queue import get_queue
from music.audio_url_retriever import get_retriever as get_audio_url_retriever
from music.audio_url_retriever import WrongUrlException

@get_bot().command(name='add')
async def _add(ctx, link):
    try:
        await _try_to_add(ctx, link)
    except WrongUrlException:
        await ctx.send('Le lien ne semble pas valide %s' % ctx.author.mention)

async def _try_to_add(ctx, link):
    url = get_audio_url_retriever().retrieve(link)
    source = discord.FFmpegPCMAudio(url)

    get_queue().add(source)

