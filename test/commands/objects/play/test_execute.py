from test.commands.objects.play.test_case_execute import TestCase

class TestPlayCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx, 'fake_link')

        self.assertTrue(self.ctx.voice_client.is_playing())
        self.assertEqual(self.ctx.sent, 'Ça marche [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Je ne suis pas connecté [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté pour ça [author.mention]')

    async def test_already_playing(self):
        await self.command.execute(self.ctx, 'fake_link')
        await self.command.execute(self.ctx, 'fake_link')

        self.assertEqual(self.ctx.sent, 'Je joue déjà un truc [author.mention]')

    async def test_wrong_link(self):
        self.command.sourceGenerator.triggerWrongLinkException = True

        await self.command.execute(self.ctx, 'wrong_link')

        self.assertEqual(self.ctx.sent, 'Le lien ne semble pas fonctionner [author.mention]')

