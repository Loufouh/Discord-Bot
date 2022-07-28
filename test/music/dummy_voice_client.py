
class DummyVoiceClient:
    _isConnected = True
    _isPaused = False
    _isPlaying = False

    afterPlay = None
    currentSource = None

    def end_playing(self):
        self.stop()

        if self.afterPlay is not None:
            self.afterPlay(None)

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

    def pause(self):
        self._isPaused = True

    def resume(self):
        self._isPaused = False

