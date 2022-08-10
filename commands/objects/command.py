from config import config

from dummies.commands.objects.command import Command_dummy

_commands = {}

def get_command(commandClass):
    global _commands

    if commandClass not in _commands.keys():
        if config['isTesting']:
            _commands[commandClass] = Command_dummy()
        else:
            _commands[commandClass] = commandClass()

    return _commands[commandClass]

def reset():
    global _commands

    for key in list(_commands.keys()):
        del _commands[key]

