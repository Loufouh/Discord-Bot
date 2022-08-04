from Bot import get_bot

from music.queue_player import get_queue_player

@get_bot().command(name='next')
async def _next(ctx):
    get_queue_player().next()

