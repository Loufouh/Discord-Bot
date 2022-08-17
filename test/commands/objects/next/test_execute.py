import unittest
import discord

from commands.objects.next import NextCommand

from music.queue import Queue

from dummies.context import Context_dummy
from dummies.queue_player import QueuePlayer_dummy

class TestNextCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()
        self.command = NextCommand()
        self.queue = Queue()
        self.player = QueuePlayer_dummy()

        self.queue.add(discord.AudioSource())
        self.player.set_queue(self.queue)

        self.command.player = self.player

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.player.play(self.ctx.voice_client)
    
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Ça marche [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_not_playing(self):
        self.ctx.voice_client.stop()

        await self.command.execute(self.ctx)

        self.assertFalse(self.player._calledNext)
        self.assertEqual(self.ctx.sent, 'Je joue rien pour l\'instant [author.mention]')

