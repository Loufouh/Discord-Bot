from test.commands.dummies.test.channel.test_case import TestCase

class TestChannel__disconnect(TestCase):
    async def test(self):
        await self.channel.connect()
        await self.channel._disconnect()

        self.assertFalse(self.channel.isConnected)
        self.assertIsNone(self.channel.ctx.voice_client)

