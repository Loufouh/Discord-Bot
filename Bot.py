from discord.ext.commands import Bot as AbsBot
from tokenHandling import *


class Bot(AbsBot):
    def __init__(self):
        super().__init__('>')

    def run(self):
        super().run(get_token())

    async def on_ready(self):
        print('Logged as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: \"{0.content}\"'.format(message))
