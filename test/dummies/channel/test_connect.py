import unittest

from dummies.channel import Channel_dummy
from dummies.context import Context_dummy

class TestChannel_connect(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.channel = Channel_dummy(self.ctx)

    async def test(self):
        await self.channel.connect()

        self.assertTrue(self.channel._isConnected)
        self.assertIsNotNone(self.channel.ctx.voice_client)

