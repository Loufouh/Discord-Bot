import discord

from Bot import get_bot

from music.audio_url_retriever import get_retriever
from music.queue_player import get_queue_player
from music.queue import Queue

import threading

bot = get_bot()
queue = Queue()

@bot.command(name='join')
async def _join(ctx):
    if ctx.author.voice is None:
        await ctx.send('Je trouve pas ton salon audio {}'.format(ctx.author.mention))
    else:
        await ctx.send('J\'arrive {} !'.format(ctx.author.mention))
        await ctx.author.voice.channel.connect()
        
@bot.command(name='play')
async def _play(ctx, musicLink):
    if ctx.voice_client is None:
        await ctx.send('Chuis pas encore connecté {}...'.format(ctx.author.mention))
    elif ctx.voice_client.is_playing():
        await ctx.send('Je joue déjà un truc {}'.format(ctx.author.mention))
    else:
        queue = Queue()

        url = get_retriever().retrieve(musicLink)
        source = discord.FFmpegPCMAudio(url)

        queue.add(source)

        get_queue_player().set_queue(queue)
        get_queue_player().play(ctx.voice_client)

@bot.command(name='stop')
async def _stop(ctx):
    ctx.voice_client.stop()

@bot.command(name='pause')
async def _pause(ctx):
    ctx.voice_client.pause()

@bot.command(name='resume')
async def _resume(ctx):
    ctx.voice_client.resume()
    
@bot.command(name='add')
async def _add(ctx, link):
    global queue

    def load():
        queue.add(get_loader().load_from_link(link))

    threading.Thread(target=load).run()

@bot.command(name='startQueue')
async def _startQueue(ctx):
    global queue

    get_queue_player().set_queue(queue)
    get_queue_player().play(ctx.voice_client)

@bot.command(name='next')
async def _next(ctx):
    get_queue_player().next()

