from Bot import get_bot

from commands.objects.leave import get_command

@get_bot().command(name='leave')
async def _leave(ctx):
    await get_command().execute(ctx)

