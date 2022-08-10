import unittest

from commands.play import _play
from commands.objects.play import get_command
from dummies.context import Context_dummy

class TestPlay(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _play(ctx, 'fake_link')

        self.assertTrue(get_command()._hasBeenExecuted)

