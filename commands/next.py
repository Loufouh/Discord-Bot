from Bot import get_bot

from commands.objects.command import get_command
from commands.objects.next import NextCommand

@get_bot().command(name='next')
async def _next(ctx):
    nextCommand = get_command(NextCommand)

    await nextCommand.execute(ctx)

