import unittest
import discord

from commands.objects.next import NextCommand

from music.queue import Queue

from dummies.context import Context_dummy
from dummies.queue_player import QueuePlayer_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        await self.setUp_context()
        self.setUp_queue()
        self.setUp_player()
        self.setUp_command()

        self.play_queue()

    async def setUp_context(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    def setUp_queue(self):
        self.queue = Queue()
        self.queue.add(discord.AudioSource())

    def setUp_player(self):
        self.player = QueuePlayer_dummy()
        self.player.set_queue(self.queue)

    def setUp_command(self):
        self.command = NextCommand()
        self.command.player = self.player

    def play_queue(self):
        self.player.play(self.ctx.voice_client)

