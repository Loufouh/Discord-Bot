from music.queue_player import get_queue_player

class NextCommand:
    def __init__(self):
        self.player = get_queue_player()

    async def execute(self, ctx):
        self.player.next()
