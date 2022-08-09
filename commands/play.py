import discord

from Bot import get_bot

from commands.objects.play import get_command

@get_bot().command(name='play')
async def _play(ctx, musicLink):
    playCommand = get_command()

    await playCommand.execute(ctx, musicLink)

