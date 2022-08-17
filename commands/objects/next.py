from commands.exceptions.exceptions import AuthorNotConnectedException, NotConnectedException, NotPlayingException

from music.queue_player import get_queue_player

from message_sender import MessageSender

class NextCommand:
    def __init__(self):
        self.player = get_queue_player()

    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté à un salon audio pour ça')
        except NotConnectedException:
            await self.messageSender.send('Je suis pas connecté au salon')
        except NotPlayingException:
            await self.messageSender.send('Je joue rien pour l\'instant')

    async def try_to_execute(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is None:
            raise NotConnectedException()
        if not ctx.voice_client.is_playing():
            raise NotPlayingException()

        self.player.next()

        await self.messageSender.send('Ça marche')

