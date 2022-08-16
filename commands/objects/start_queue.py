from music.queue_player import QueuePlayer

class StartQueueCommand:
    def __init__(self):
        self.player = QueuePlayer()

    async def execute(self, ctx):
        self.player.play(ctx.voice_client)

