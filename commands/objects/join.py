from commands.exceptions.exceptions import AuthorNotConnectedException, AlreadyConnectedException
from dummies.commands.objects.command import Command_dummy

class JoinCommand:
    async def execute(self, ctx):
        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await ctx.reply('Tu dois être connecté à un salon audio pour ça')
        except AlreadyConnectedException:
            await ctx.reply('Je suis déjà connecté') 

    async def try_to_execute(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is not None:
            raise AlreadyConnectedException()

        await ctx.reply('J\'arrive !')
        await ctx.author.voice.channel.connect()

