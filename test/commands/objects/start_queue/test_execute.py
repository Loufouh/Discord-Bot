import unittest

from commands.objects.start_queue import StartQueueCommand

from dummies.queue_player import QueuePlayer_dummy
from dummies.context import Context_dummy

from music.queue import get_queue

class TestStartQueueCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.player = QueuePlayer_dummy()
        self.command = StartQueueCommand()

        get_queue().add('source')

        self.command.player = self.player

        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledPlay)
        self.assertEqual(self.player.voiceClient, self.ctx.voice_client)
        self.assertEqual(self.player.queue, get_queue())
        self.assertEqual(self.ctx.sent, 'C\'est parti ! [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_empty_queue(self):
        get_queue().reset()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'La file est vide [author.mention]')

