
class Command_dummy:
    def __init__(self):
        self._hasBeenExecuted = False

    async def execute(self, ctx, *args):
        self._hasBeenExecuted = True

