import unittest
import discord

from commands.objects.next import NextCommand

from dummies.context import Context_dummy
from dummies.queue_player import QueuePlayer_dummy

class TestNextCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.command = NextCommand()
        self.player = QueuePlayer_dummy()

        self.command.player = self.player
    
    async def test(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledNext)

