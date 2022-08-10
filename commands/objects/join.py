from commands.exceptions.exceptions import AuthorNotConnectedException, AlreadyConnectedException
from dummies.commands.objects.command import Command_dummy

class JoinCommand:
    async def execute(self, ctx):
        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await ctx.send('Tu dois être connecté à un salon audio pour ça %s' % ctx.author.mention)
        except AlreadyConnectedException:
            await ctx.send('Je suis déjà connecté %s' % ctx.author.mention) 

    async def try_to_execute(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is not None:
            raise AlreadyConnectedException()

        await ctx.send('J\'arrive ! %s' % ctx.author.mention)
        await ctx.author.voice.channel.connect()

