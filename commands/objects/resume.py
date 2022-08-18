from commands.exceptions.exceptions import AuthorNotConnectedException, NotConnectedException, NotPlayingException, NotPausedException
from message_sender import MessageSender

class ResumeCommand:
    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)
        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté à un salon audio pour ça')
        except NotConnectedException:
            await self.messageSender.send('Je suis pas connecté au salon')
        except NotPlayingException:
            await self.messageSender.send('Je n\'ai rien à jouer pour l\'instant')
        except NotPausedException:
            await self.messageSender.send('Ce n\'est pas en pause')

    async def try_to_execute(self, ctx):
        self.verify_context(ctx)

        ctx.voice_client.resume()

        await self.messageSender.send('C\'est reparti !')

    def verify_context(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is None:
            raise NotConnectedException()
        if not ctx.voice_client.is_playing():
            raise NotPlayingException()
        if not ctx.voice_client.is_paused():
            raise NotPausedException()

