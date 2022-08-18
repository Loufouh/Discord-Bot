import unittest

from commands.objects.start_queue import StartQueueCommand

from dummies.queue_player import QueuePlayer_dummy
from dummies.context import Context_dummy

from music.queue import get_queue

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        await self.setUp_context()
        self.setUp_player()
        self.setUp_queue()
        self.setUp_command()

    async def setUp_context(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    def setUp_player(self):
        self.player = QueuePlayer_dummy()

    def setUp_queue(self):
        get_queue().add('source')

    def setUp_command(self):
        self.command = StartQueueCommand()
        self.command.player = self.player

