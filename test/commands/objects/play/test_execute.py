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

        self.assertEqual(self.ctx.replied, 'Ça marche')
        self.assertTrue(self.ctx.voice_client.is_playing())

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.replied, 'Je joue déjà un truc')

    async def test_already_playing(self):
        await self.command.execute(self.ctx, 'fake_link')
        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.replied, 'Je joue déjà un truc')

    async def test_wrong_link(self):
        self.command.sourceGenerator.triggerWrongLinkException = True

        await self.command.execute(self.ctx, 'wrong_link')

        self.assertEqual(self.ctx.replied, 'Le lien ne semble pas fonctionner')

