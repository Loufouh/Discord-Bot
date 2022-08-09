
class PlayCommand_dummy:
    def __init__(self):
        self._hasBeenExecuted = False

    async def execute(self, ctx, musicLink):
        self._hasBeenExecuted = True

