from Bot import get_bot

from commands.objects.resume import ResumeCommand
from commands.objects.command import get_command

@get_bot().command(name='resume')
async def _resume(ctx):
    command = get_command(ResumeCommand)

    await command.execute(ctx)
 
