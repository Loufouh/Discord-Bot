import unittest
import discord

from commands.objects.stop import StopCommand
from commands.objects.play import PlayCommand

from dummies.context import Context_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.setUp_command()
        await self.setUp_context()

    def setUp_command(self):
        self.command = StopCommand()

    async def setUp_context(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())

