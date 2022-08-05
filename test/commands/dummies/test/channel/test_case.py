import unittest

from test.commands.dummies.channel import Channel_dummy
from test.commands.dummies.context import Context_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        ctx = Context_dummy()
        self.channel = Channel_dummy(ctx)

