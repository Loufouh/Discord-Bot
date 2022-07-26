from discord.ext import commands
from token_handling import *

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='>')

    def run(self):
        super().run(get_token())

    async def on_ready(self):
        print('Logged as {0}!'.format(self.user))

instance = None

def get_bot():
    global instance

    if instance is None:
        instance = Bot()

    return instance

