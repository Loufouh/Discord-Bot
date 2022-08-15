import unittest

from commands.resume import _resume

from dummies.context import Context_dummy
from commands.objects.resume import ResumeCommand
from commands.objects.command import get_command

class TestResume(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _resume(ctx)

        self.assertTrue(get_command(ResumeCommand)._hasBeenExecuted)

