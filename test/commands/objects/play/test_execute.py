import unittest

from commands.objects.play import PlayCommand

from dummies.context import Context_dummy
from dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestPlayCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.command = PlayCommand()

        self.command.sourceGenerator = AudioSourceGenerator_dummy()
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    async def test_normal(self):
        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Ça marche [author.mention]')
        self.assertTrue(self.ctx.voice_client.is_playing())

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Je ne suis pas connecté [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté pour ça [author.mention]')

    async def test_already_playing(self):
        await self.command.execute(self.ctx, 'fake_link')
        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Je joue déjà un truc [author.mention]')

    async def test_wrong_link(self):
        self.command.sourceGenerator.triggerWrongLinkException = True

        await self.command.execute(self.ctx, 'wrong_link')

        self.assertEqual(self.ctx.sent, 'Le lien ne semble pas fonctionner [author.mention]')

