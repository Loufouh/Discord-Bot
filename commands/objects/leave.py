from commands.exceptions.exceptions import NotConnectedException
from dummies.commands.objects.command import Command_dummy

class LeaveCommand:
    async def execute(self, ctx):
        try:
            await self.try_to_execute(ctx)
        except NotConnectedException:
            await ctx.reply('Chuis pas connecté')

    async def try_to_execute(self, ctx):
        if ctx.voice_client is None:
            raise NotConnectedException()

        await ctx.reply('Bye !')
        await ctx.voice_client.disconnect()

