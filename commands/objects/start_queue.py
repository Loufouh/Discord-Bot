from music.queue_player import QueuePlayer
from music.queue import get_queue

class StartQueueCommand:
    def __init__(self):
        self.player = QueuePlayer()

    async def execute(self, ctx):
        self.player.set_queue(get_queue())
        self.player.play(ctx.voice_client)

