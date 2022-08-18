import unittest
import discord

from commands.objects.resume import ResumeCommand

from dummies.context import Context_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        await self.setUp_context()
        self.setUp_command()

    async def setUp_context(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())
        self.ctx.voice_client.pause()

    def setUp_command(self):
        self.command = ResumeCommand()

