import unittest

from commands.objects.start_queue import StartQueueCommand

from dummies.queue_player import QueuePlayer_dummy
from dummies.context import Context_dummy

class TestStartQueueCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.player = QueuePlayer_dummy()
        self.command = StartQueueCommand()

        self.command.player = self.player

        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    async def test(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledPlay)
        self.assertEqual(self.player.voiceClient, self.ctx.voice_client)

