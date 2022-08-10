import unittest

from commands.play import _play

from dummies.context import Context_dummy
from commands.objects.play import PlayCommand
from commands.objects.command import get_command

class TestPlay(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _play(ctx, 'fake_link')

        self.assertTrue(get_command(PlayCommand)._hasBeenExecuted)

