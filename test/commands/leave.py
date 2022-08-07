import unittest

from test.commands.dummies.context import Context_dummy

from commands.leave import _leave

class TestLeave(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()

    async def test_not_connected(self):
        await _leave(self.ctx)

        self.assert_sent_connected_message()

    async def test_normal(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        await _leave(self.ctx)

        self.assert_sent_bye_message()

    def assert_sent_connected_message(self):
        self.assertEqual(self.ctx.sent, 'Chuis pas connecté [author.mention]')

    def assert_sent_bye_message(self):
        self.assertEqual(self.ctx.sent, 'Bye ! [author.mention]')

