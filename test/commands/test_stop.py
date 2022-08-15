import unittest

from commands.stop import _stop

from dummies.context import Context_dummy
from commands.objects.stop import StopCommand
from commands.objects.command import get_command

class TestStop(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _stop(ctx)

        self.assertTrue(get_command(StopCommand)._hasBeenExecuted)

