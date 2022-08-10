from config import config

from dummies.commands.objects.command import Command_dummy

_commands = {}

def get_command(cls):
    global _commands

    if cls not in _commands.keys():
        if config['isTesting']:
            _commands[cls] = Command_dummy()
        else:
            _commands[cls] = cls()

    return _commands[cls]

def reset():
    global _commands

    for key in list(_commands.keys()):
        del _commands[key]

