from commands.exceptions.exceptions import NotConnectedException
from dummies.commands.objects.command import Command_dummy

from message_sender import MessageSender

class LeaveCommand:
    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except NotConnectedException:
            await self.messageSender.send('Chuis pas connecté')

    async def try_to_execute(self, ctx):
        if ctx.voice_client is None:
            raise NotConnectedException()

        await self.messageSender.send('Bye !')
        await ctx.voice_client.disconnect()

