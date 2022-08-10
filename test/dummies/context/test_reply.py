import unittest

from dummies.context import Context_dummy

class TestContext_reply(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.context = Context_dummy()

    async def test_reply_once(self):
        await self.context.reply('test message')
        self.assertEqual(self.context.replied, 'test message')

