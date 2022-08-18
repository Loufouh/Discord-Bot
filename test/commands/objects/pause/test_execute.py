from test.commands.objects.pause.test_case import TestCase

class TestPauseCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledPause)
        self.assertEqual(self.ctx.sent, 'Je mets en pause [author.mention]')

    async def test_already_paused(self):
        await self.command.execute(self.ctx)
        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledPause)
        self.assertTrue(self.ctx.voice_client.is_paused())
        self.assertEqual(self.ctx.sent, 'C\'est déjà en pause [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je ne joue rien pour l\'instant [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté au salon pour ça [author.mention]')

