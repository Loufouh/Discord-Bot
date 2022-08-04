
class Channel_dummy:
    def __init__(self):
        self.isConnected = False

    async def connect(self):
        self.isConnected = True

