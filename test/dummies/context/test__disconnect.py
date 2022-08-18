from test.dummies.context.test_case import TestCase

class TestContext__disconnect(TestCase):
    async def test(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        await self.ctx._disconnect()

        self.assertIsNone(self.ctx.voice_client)

