from commands.exceptions.exceptions import AuthorNotConnectedException, NotConnectedException, AlreadyPlayingException

from message_sender import MessageSender

from music.audio_source_generator.common import AudioSourceGenerator, WrongLinkException

from dummies.commands.objects.command import Command_dummy

class PlayCommand:
    def __init__(self):
        self.sourceGenerator = AudioSourceGenerator()

    async def execute(self, ctx, musicLink):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx, musicLink)
        except AuthorNotConnectedException:
            await self.messageSender.send('Tu dois être connecté pour ça')
        except NotConnectedException:
            await self.messageSender.send('Je ne suis pas connecté')
        except AlreadyPlayingException:
            await self.messageSender.send('Je joue déjà un truc')
        except WrongLinkException:
            await self.messageSender.send('Le lien ne semble pas fonctionner')

    async def try_to_execute(self, ctx, musicLink):
        self.verify_context(ctx)

        source = self.sourceGenerator.generate_from_link(musicLink)

        await self.messageSender.send('Ça marche')
        ctx.voice_client.play(source)

    def verify_context(self, ctx):
        if ctx.author.voice is None:
            raise AuthorNotConnectedException()
        if ctx.voice_client is None:
            raise NotConnectedException()
        if ctx.voice_client.is_playing():
            raise AlreadyPlayingException()

