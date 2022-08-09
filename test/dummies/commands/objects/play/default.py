import unittest

from dummies.commands.objects.play import PlayCommand_dummy

class TestPlayCommand_default(unittest.TestCase):
    def test(self):
        command = PlayCommand_dummy()
        self.assertFalse(command._hasBeenExecuted)

