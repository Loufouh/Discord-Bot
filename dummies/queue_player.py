
class QueuePlayer_dummy:
    def __init__(self):
        self._calledNext = False

    def next(self):
        self._calledNext = True

