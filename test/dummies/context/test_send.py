from test.dummies.context.test_case import TestCase

class TestContext_send(TestCase):
    async def test_send_one(self):
        await self.ctx.send('test message')
        self.assertEqual(self.ctx.sent, 'test message')

    async def test_send_two(self):
        await self.ctx.send('first message')
        await self.ctx.send('second message')

        self.assertEqual(self.ctx.sent, 'second message')

