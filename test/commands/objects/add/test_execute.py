import unittest
import discord

from commands.objects.add import AddCommand

from music.queue import get_queue

from dummies.context import Context_dummy
from dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestAddCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.command = AddCommand()

        self.command.sourceGenerator = AudioSourceGenerator_dummy()
        self.ctx = Context_dummy()

        self.queue = get_queue()
        self.queue.reset()

    async def test_normal(self):
        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Je l\'ajoute à la file [author.mention]')
        self.assertEqual(self.queue.get_size(), 1)
        self.assertIsInstance(self.queue.get_head(), discord.AudioSource)

    async def test_normal_100_times(self):
        for i in range(100):
            await self.command.execute(self.ctx, 'fake_link')

            self.assertEqual(self.ctx.sent, 'Je l\'ajoute à la file [author.mention]')
            self.assertIsInstance(self.queue.get_head(), discord.AudioSource)
            self.assertEqual(self.queue.get_size(), i + 1)

    async def test_wrong_link(self):
        self.command.sourceGenerator.triggerWrongLinkException = True

        await self.command.execute(self.ctx, 'wrong_link')

        self.assertEqual(self.ctx.sent, 'Le lien ne semble pas fonctionner [author.mention]')

