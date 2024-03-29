from Bot import get_bot

from discord.errors import ClientException
from commands.exceptions.exceptions import AuthorNotConnectedException, AlreadyConnectedException

from commands.objects.join import JoinCommand
from commands.objects.command import get_command

@get_bot().command(name='join')
async def _join(ctx):
    await get_command(JoinCommand).execute(ctx)

