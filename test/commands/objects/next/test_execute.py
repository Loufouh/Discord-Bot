import unittest
import discord

from commands.objects.next import NextCommand

from music.queue import get_queue
from music.queue_player import get_queue_player

from dummies.context import Context_dummy

class TestNextCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.command = NextCommand()
        self.queue = get_queue()
        self.player = get_queue_player()

        self.player.set_queue(self.queue)

        self.sources = [discord.AudioSource() for _ in range(100)]

        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()


    async def test_normal(self):
        for i in range(2):
           self.queue.add(self.sources[i])

        self.player.play(self.ctx.voice_client)

        await self.command.execute(self.ctx)

        self.assertTrue(self.ctx.voice_client.is_playing())
        self.assertEqual(self.ctx.voice_client.source, self.sources[1])

