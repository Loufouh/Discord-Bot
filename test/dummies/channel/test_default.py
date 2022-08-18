import unittest

from dummies.context import Context_dummy
from dummies.channel import Channel_dummy

class TestChannel_default(unittest.TestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.channel = Channel_dummy(self.ctx)

    def test(self):
        self.assertEqual(self.channel.ctx, self.ctx)
        self.assertFalse(self.channel._isConnected)

