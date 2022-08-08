import unittest

from dummies.context import Context_dummy
from test.commands.dummies.channel import Channel_dummy

class TestChannel_default(unittest.TestCase):
    def test(self):
        ctx = Context_dummy()
        channel = Channel_dummy(ctx)

        self.assertEqual(channel.ctx, ctx)
        self.assertFalse(channel._isConnected)

