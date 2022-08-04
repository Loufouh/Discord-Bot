
class VoiceClient_dummy:
    def __init__(self):
        self._isConnected = True
        self._isPaused = False
        self._isPlaying = False

        self.afterPlay = None
        self.currentSource = None

    def is_connected(self):
        return self._isConnected

    def is_paused(self):
        return self._isPaused

    def is_playing(self):
        return self._isPlaying

    
    def play(self, source, after=None):
        self._isPlaying = True

        self.currentSource = source
        self.afterPlay = after

    def stop(self):
        self._isPlaying = False
        self.currentSource = None

        self.trigger_after_play()

    def pause(self):
        self._isPaused = True

    def resume(self):
        self._isPaused = False

    def trigger_after_play(self):
        if self.afterPlay is not None:
            self.afterPlay(None)

