import unittest

from commands.start_queue import _startQueue

from dummies.context import Context_dummy
from commands.objects.start_queue import StartQueueCommand
from commands.objects.command import get_command

class Teststart_queue(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _startQueue(ctx)

        self.assertTrue(get_command(StartQueueCommand)._hasBeenExecuted)

