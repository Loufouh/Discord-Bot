import unittest

from dummies.queue_player import QueuePlayer_dummy
from dummies.context import Context_dummy

class TestQueuePlayer_play(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.player = QueuePlayer_dummy()
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    def test(self):
        self.player.play(self.ctx.voice_client)

        self.assertEqual(self.player.voiceClient, self.ctx.voice_client)
        self.assertTrue(self.player._calledPlay)

        self.assertTrue(self.ctx.voice_client.is_playing())

