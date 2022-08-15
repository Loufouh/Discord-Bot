import unittest
import discord

from commands.objects.pause import PauseCommand

from dummies.context import Context_dummy

class TestPauseCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())

    async def test(self):
        command = PauseCommand()

        await command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledPause)

