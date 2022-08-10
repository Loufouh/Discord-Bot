from commands.exceptions.exceptions import NotConnectedException, AlreadyPlayingException

from music.audio_source_generator import AudioSourceGenerator
from music.audio_source_generator import WrongLinkException

from dummies.commands.objects.command import Command_dummy

class PlayCommand:
    def __init__(self):
        self.sourceGenerator = AudioSourceGenerator()

    async def execute(self, ctx, musicLink):
        try:
            await self.try_to_execute(ctx, musicLink)
        except NotConnectedException:
            await ctx.reply('Je joue déjà un truc')
        except AlreadyPlayingException:
            await ctx.reply('Je joue déjà un truc')
        except WrongLinkException:
            await ctx.reply('Le lien ne semble pas fonctionner')

    async def try_to_execute(self, ctx, musicLink):
        if ctx.voice_client is None:
            raise NotConnectedException()
        if ctx.voice_client.is_playing():
            raise AlreadyPlayingException()

        source = self.sourceGenerator.generate_from_link(musicLink)

        await ctx.reply('Ça marche')

        ctx.voice_client.play(source)

