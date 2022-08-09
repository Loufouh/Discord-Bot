import unittest

from commands.objects.play import get_command, reset, _command

class TestPlayCommand_reset(unittest.TestCase):
    def test(self):
        get_command()
        reset()

        self.assertIsNone(_command)
        
