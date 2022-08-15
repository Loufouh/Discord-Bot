import unittest

from dummies.context import Context_dummy

class TestVoiceProtocol_disconnect(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await ctx._connect_author()
        await ctx._connect()

        await ctx.voice_client.disconnect()

        self.assertIsNone(ctx.voice_client)
        self.assertIsNotNone(ctx.author.voice)
        
        self.assertTrue(ctx.author.voice.channel._isConnected)

