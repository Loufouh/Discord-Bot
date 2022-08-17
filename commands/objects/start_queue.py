from commands.exceptions.exceptions import AuthorNotConnectedException, NotConnectedException, EmptyQueueException

from message_sender import MessageSender

from music.queue_player import QueuePlayer
from music.queue import get_queue

class StartQueueCommand:
    def __init__(self):
        self.player = QueuePlayer()

    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté à un salon audio pour ça')
        except NotConnectedException:
            await self.messageSender.send('Je suis pas connecté au salon')
        except EmptyQueueException:
            await self.messageSender.send('La file est vide')

    async def try_to_execute(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is None:
            raise NotConnectedException()
        if get_queue().get_size() == 0:
            raise EmptyQueueException()

        self.player.set_queue(get_queue())
        self.player.play(ctx.voice_client)
        await self.messageSender.send('C\'est parti !')

