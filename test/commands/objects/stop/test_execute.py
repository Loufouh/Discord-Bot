import unittest
import discord

from commands.objects.stop import StopCommand
from commands.objects.play import PlayCommand

from dummies.context import Context_dummy
from dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestStopCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()

        self.command = StopCommand()

    async def test_normal(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        self.ctx.voice_client.play(discord.AudioSource())

        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client._calledStop)

