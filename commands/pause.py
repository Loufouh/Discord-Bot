from Bot import get_bot

from commands.objects.pause import PauseCommand
from commands.objects.command import get_command

@get_bot().command(name='pause')
async def _pause(ctx):
    pauseCommand = get_command(PauseCommand)

    await pauseCommand.execute(ctx)

