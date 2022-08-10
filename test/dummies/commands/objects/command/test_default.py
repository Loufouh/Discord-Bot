import unittest

from dummies.commands.objects.command import Command_dummy

class TestCommand_default(unittest.IsolatedAsyncioTestCase):
    def test(self):
        command = Command_dummy()

        self.assertFalse(command._hasBeenExecuted)

