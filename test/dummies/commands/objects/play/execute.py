import unittest

from dummies.commands.objects.play import PlayCommand_dummy
from dummies.context import Context_dummy

class TestPlayCommand_execute(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        command = PlayCommand_dummy()

        await command.execute(ctx, 'fake_link')

        self.assertTrue(command._hasBeenExecuted)

