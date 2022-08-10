import discord

from Bot import get_bot

from commands.objects.command import get_command
from commands.objects.play import PlayCommand

@get_bot().command(name='play')
async def _play(ctx, musicLink):
    playCommand = get_command(PlayCommand)

    await playCommand.execute(ctx, musicLink)

