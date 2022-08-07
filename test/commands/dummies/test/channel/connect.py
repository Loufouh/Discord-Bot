from test.commands.dummies.test.channel.test_case import TestCase

class TestChannel_connect(TestCase):
    async def test(self):
        await self.channel.connect()

        self.assertTrue(self.channel._isConnected)
        self.assertIsNotNone(self.channel.ctx.voice_client)

