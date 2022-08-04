import discord

from Bot import get_bot

from music.queue import get_queue
from music.audio_url_retriever import get_retriever as get_audio_url_retriever

@get_bot().command(name='add')
async def _add(ctx, link):
    url = get_audio_url_retriever().retrieve(link)
    source = discord.FFmpegPCMAudio(url)

    get_queue().add(source)

