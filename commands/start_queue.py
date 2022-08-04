from Bot import get_bot

from music.queue_player import get_queue_player
from music.queue import get_queue

@get_bot().command(name='startQueue')
async def _startQueue(ctx):
    get_queue_player().set_queue(get_queue())
    get_queue_player().play(ctx.voice_client)

