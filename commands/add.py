import discord

from Bot import get_bot

from commands.objects.command import get_command
from commands.objects.add import AddCommand

@get_bot().command(name='add')
async def _add(ctx, musicLink):
    addCommand = get_command(AddCommand)

    await addCommand.execute(ctx, musicLink)

