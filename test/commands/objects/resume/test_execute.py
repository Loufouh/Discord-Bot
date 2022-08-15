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

    async def test(self):
        command = ResumeCommand()

        await command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledResume)

