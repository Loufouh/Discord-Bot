from test.commands.objects.stop.test_case import TestCase

class TestStopCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledStop)
        self.assertEqual(self.ctx.sent, 'Ok [author.mention]')

    async def test_not_conntected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect()
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté au salon pour ça [author.mention]')

    async def test_not_playing(self):
        self.ctx.voice_client.stop()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je joue rien pour l\'instant [author.mention]')

