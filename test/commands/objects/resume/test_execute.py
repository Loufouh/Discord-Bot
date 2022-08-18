from test.commands.objects.resume.test_case import TestCase

class TestResumeCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledResume)
        self.assertEqual(self.ctx.sent, 'C\'est reparti ! [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()
        
        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_not_playing(self):
        self.ctx.voice_client.stop()

        await self.command.execute(self.ctx)

        self.assertFalse(self.ctx.voice_client._calledResume)
        self.assertEqual(self.ctx.sent, 'Je n\'ai rien à jouer pour l\'instant [author.mention]')

    async def test_not_paused(self):
        self.ctx.voice_client.resume()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Ce n\'est pas en pause [author.mention]')

