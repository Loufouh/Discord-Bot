import unittest

from commands.objects.join import get_command, reset, _command

class TestLeaveCommand_reset(unittest.TestCase):
    def test(self):
        get_command()
        reset()

        self.assertIsNone(_command)
        
