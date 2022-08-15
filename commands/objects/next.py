from music.queue_player import get_queue_player

class NextCommand:
    async def execute(self, ctx):
        get_queue_player().next()
