import unittest

from test.commands.dummies.context import Context_dummy

class TestContext_send(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.context = Context_dummy()

    async def test_send_one(self):
        await self.context.send('test message')
        self.assertEqual(self.context.sent, 'test message')

    async def test_send_two(self):
        await self.context.send('first message')
        await self.context.send('second message')

        self.assertEqual(self.context.sent, 'second message')

