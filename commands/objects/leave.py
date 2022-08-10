from config import config

from commands.exceptions.exceptions import NotConnectedException
from dummies.commands.objects.command import Command_dummy

class LeaveCommand:
    async def execute(self, ctx):
        try:
            await self.try_to_execute(ctx)
        except NotConnectedException:
            await ctx.send('Chuis pas connecté %s' % ctx.author.mention)

    async def try_to_execute(self, ctx):
        if ctx.voice_client is None:
            raise NotConnectedException()

        await ctx.send('Bye ! %s' % ctx.author.mention)
        await ctx.voice_client.disconnect()

_command = None

def get_command():
    global _command

    if _command is None:
        if config['isTesting']:
            _command = Command_dummy()
        else:
            _command = LeaveCommand()

    return _command

def reset():
    global _command

    _command = None

