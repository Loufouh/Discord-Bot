
from message_sender import MessageSender

from music.audio_source_generator.common import AudioSourceGenerator, WrongLinkException
from music.queue import get_queue

class AddCommand:
    def __init__(self):
        self.sourceGenerator = AudioSourceGenerator()

    async def execute(self, ctx, musicLink):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx, musicLink)
        except WrongLinkException:
            await self.messageSender.send('Le lien ne semble pas fonctionner')

    async def try_to_execute(self, ctx, musicLink):

        await self.messageSender.send('Je l\'ajoute à la file')

        source = self.sourceGenerator.generate_from_link(musicLink)
        get_queue().add(source)

