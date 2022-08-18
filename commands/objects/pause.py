from commands.exceptions.exceptions import AlreadyPausedException, AuthorNotConnectedException, NotConnectedException

from message_sender import MessageSender

class PauseCommand:
    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except NotConnectedException:
            await self.messageSender.send('Je ne joue rien pour l\'instant')
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté au salon pour ça')
        except AlreadyPausedException:
            await self.messageSender.send('C\'est déjà en pause')

    async def try_to_execute(self, ctx):
        self.verify_context(ctx)

        ctx.voice_client.pause()
        await self.messageSender.send('Je mets en pause')

    def verify_context(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is None:
            raise NotConnectedException()
        if ctx.voice_client.is_paused():
            raise AlreadyPausedException()

