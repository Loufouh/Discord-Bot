import unittest
import discord

from commands.objects.pause import PauseCommand

from dummies.context import Context_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.command = PauseCommand()
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())

