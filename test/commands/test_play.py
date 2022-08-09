import unittest

from commands.play import _play
from dummies.context import Context_dummy

from commands.objects.play import get_command as get_play_command

class TestPlay(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await _play(ctx, 'fake_link')

        self.assertTrue(get_play_command()._hasBeenExecuted)

