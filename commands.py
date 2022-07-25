import os
import youtube_mp3_download
import discord

from Bot import get_bot

bot = get_bot()

@bot.command(name='hello')
async def _hello(ctx):
    await ctx.send('Hello {}'.format(ctx.author.mention))

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
        filename = youtube_mp3_download.download(musicLink)

        audioSource = discord.FFmpegPCMAudio(filename)
        ctx.voice_client.play(audioSource)

