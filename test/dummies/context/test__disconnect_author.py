from test.dummies.context.test_case import TestCase

class TestContext__disconnect_author(TestCase):
    async def test(self):
        await self.ctx._connect_author()

        await self.ctx._disconnect_author()

        self.assertIsNone(self.ctx.author.voice)

