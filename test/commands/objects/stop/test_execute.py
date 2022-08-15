import unittest
import discord

from commands.objects.stop import StopCommand
from commands.objects.play import PlayCommand

from dummies.context import Context_dummy

class TestStopCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        self.command = StopCommand()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())

    async def test(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledStop)

