from test.commands.dummies.voice_state import VoiceState_dummy
from test.commands.dummies.author import Author_dummy

class Context_dummy:
    def __init__(self):
        self.author = Author_dummy()
        self.voice_client = None

        self.sent = ''

    async def send(self, msg):
        self.sent = msg

    async def _connect_author(self):
        self.author.voice = VoiceState_dummy(self)

    async def _connect(self):
        await self.author.voice.channel.connect()

