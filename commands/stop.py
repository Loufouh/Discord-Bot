from Bot import get_bot

from commands.objects.command import get_command
from commands.objects.stop import StopCommand

@get_bot().command(name='stop')
async def _stop(ctx):
    stopCommand = get_command(StopCommand)

    await stopCommand.execute(ctx)

