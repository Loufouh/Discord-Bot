
class QueuePlayer:
    queue = None

    def play(self, voiceClient):
        def after(error):
            self.play(voiceClient)

        source = self.queue.pop()

        if source is not None:
            voiceClient.play(source, after=after)

    def set_queue(self, queue):
        self.queue = queue

queuePlayer = None

def get_queue_player():
    global queuePlayer

    if queuePlayer is None:
        queuePlayer = QueuePlayer()

    return queuePlayer

