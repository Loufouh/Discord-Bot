import discord

from Bot import get_bot

from music.audio_url_retriever import get_retriever as get_audio_url_retriever
from music.queue_player import get_queue_player
from music.queue import Queue

@get_bot().command(name='play')
async def _play(ctx, musicLink):
    if ctx.voice_client is None:
        await ctx.send('Chuis pas encore connecté %s' % ctx.author.mention)
    elif ctx.voice_client.is_playing():
        await ctx.send('Je joue déjà un truc %s' % ctx.author.mention)
    else:
        queue = Queue()

        url = get_audio_url_retriever().retrieve(musicLink)
        source = discord.FFmpegPCMAudio(url)

        queue.add(source)

        get_queue_player().set_queue(queue)
        get_queue_player().play(ctx.voice_client)

