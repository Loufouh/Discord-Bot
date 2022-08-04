
class Author:
    voice = None
    mention = '[mention]'

class Context_dummy:
    sent = ''
    author = Author()

    async def send(self, msg):
        self.sent = msg

