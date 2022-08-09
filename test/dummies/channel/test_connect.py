import unittest

from dummies.channel import Channel_dummy
from dummies.context import Context_dummy

class TestChannel_connect(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        channel = Channel_dummy(ctx)

        await channel.connect()

        self.assertTrue(channel._isConnected)
        self.assertIsNotNone(channel.ctx.voice_client)

