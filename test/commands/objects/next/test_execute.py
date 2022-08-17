from test.commands.objects.next.test_case_execute import TestCase

class TestNextCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Ça marche [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_not_playing(self):
        self.ctx.voice_client.stop()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Je joue rien pour l\'instant [author.mention]')

