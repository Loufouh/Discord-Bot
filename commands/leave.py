from Bot import get_bot

from commands.objects.command import get_command
from commands.objects.leave import LeaveCommand

@get_bot().command(name='leave')
async def _leave(ctx):
    await get_command(LeaveCommand).execute(ctx)

