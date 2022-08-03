
class QueuePlayer:
    voiceClient = None
    queue = None

    def play(self, voiceClient):
        self.voiceClient = voiceClient

        source = self.queue.pop()

        if source is not None:
            voiceClient.play(
                source,
                after=lambda e : self.play(voiceClient)
            )

    def next(self):
        if self.voiceClient is not None:
            self.voiceClient.stop()

    def set_queue(self, queue):
        self.queue = queue

queuePlayer = None

def get_queue_player():
    global queuePlayer

    if queuePlayer is None:
        queuePlayer = QueuePlayer()

    return queuePlayer
