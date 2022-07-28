from Bot import get_bot

from music.loader import get_loader
from music.queue_player import get_queue_player
from music.queue import Queue

bot = get_bot()
queue = Queue()

@bot.command(name='join')
async def _join(ctx):
    voiceChannel = ctx.author.voice.channel

    if voiceChannel is None:
        await ctx.send('Je trouve pas ton salon audio...')
    else:
        await ctx.send('J\'arrive {} !'.format(ctx.author.mention))
        
@bot.command(name='play')
async def _play(ctx, musicLink):
    if ctx.voice_client is None:
        await ctx.send('Chuis pas encore connecté {}...'.format(ctx.author.mention))
    elif ctx.voice_client.is_playing():
        await ctx.send('Je joue déjà un truc {}'.format(ctx.author.mention))
    else:
        queue = Queue()
        queue.add(get_loader().load_from_link(musicLink))

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

    queue.add(get_loader().load_from_link(link))

@bot.command(name='startQueue')
async def _startQueue(ctx):
    global queue

    get_queue_player().set_queue(queue)
    get_queue_player().play(ctx.voice_client)

