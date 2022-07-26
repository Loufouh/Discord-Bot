from Bot import get_bot
from music.downloader.downloader import get_downloader
from music.play import play as play_music

bot = get_bot()

@bot.command(name='join')
async def _join(ctx):
    voiceChannel = ctx.author.voice.channel

    if voiceChannel is None:
        await ctx.send('Je trouve pas ton salon audio...')
    else:
        await ctx.send('J\'arrive {} !'.format(ctx.author.mention))
        client = await ctx.author.voice.channel.connect()
        
@bot.command(name='play')
async def _play(ctx, musicLink):
    if ctx.voice_client is None:
        await ctx.send('Chuis pas encore connecté {}...'.format(ctx.author.mention))
    else:
        play_music(
            ctx.voice_client,
            get_downloader().get_by_link(musicLink)
        )

@bot.command(name='pause')
async def _pause(ctx):
    ctx.voice_client.pause()

@bot.command(name='resume')
async def _resume(ctx):
    ctx.voice_client.resume()
    

@bot.command(name='test')
async def _test(ctx):
    play_music(
            ctx.voice_client,
            'music_files/test.mp3'
    );
