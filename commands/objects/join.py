from commands.exceptions.exceptions import AuthorNotConnectedException, AlreadyConnectedException
from dummies.commands.objects.command import Command_dummy

from message_sender import MessageSender

class JoinCommand:
    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté à un salon audio pour ça')
        except AlreadyConnectedException:
            await self.messageSender.send('Je suis déjà connecté') 

    async def try_to_execute(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is not None:
            raise AlreadyConnectedException()

        await self.messageSender.send('J\'arrive !')
        await ctx.author.voice.channel.connect()

