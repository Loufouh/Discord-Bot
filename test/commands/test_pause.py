import unittest

from commands.pause import _pause

from dummies.context import Context_dummy
from commands.objects.pause import PauseCommand
from commands.objects.command import get_command

class TestPause(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _pause(ctx)

        self.assertTrue(get_command(PauseCommand)._hasBeenExecuted)

