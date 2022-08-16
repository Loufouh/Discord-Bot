from Bot import get_bot

from commands.objects.start_queue import StartQueueCommand
from commands.objects.command import get_command

@get_bot().command(name='startQueue')
async def _startQueue(ctx):
    startQueueCommand = get_command(StartQueueCommand)

    await startQueueCommand.execute(ctx)

