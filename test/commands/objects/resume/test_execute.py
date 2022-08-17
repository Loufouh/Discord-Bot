import unittest
import discord

from commands.objects.resume import ResumeCommand

from dummies.context import Context_dummy

class TestResumeCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())
        self.ctx.voice_client.pause()

    async def test_normal(self):
        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledResume)
        self.assertEqual(self.ctx.sent, 'C\'est reparti ! [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_not_playing(self):
        self.ctx.voice_client.stop()

        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertFalse(self.ctx.voice_client._calledResume)
        self.assertEqual(self.ctx.sent, 'Je n\'ai rien à jouer pour l\'instant [author.mention]')

    async def test_not_paused(self):
        self.ctx.voice_client.resume()

        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Ce n\'est pas en pause [author.mention]')

