import discord

def emptyFunc(error):
    pass

class VoiceClient_dummy:
    def __init__(self, ctx):
        self.ctx = ctx
        self._isPlaying = False
        self.source = None
        self._afterPlayFunc = emptyFunc
        self._calledStop = False

    async def disconnect(self):
        await self.ctx._disconnect()
    
    def play(self, source, after=emptyFunc):
        if self._isPlaying:
            raise discord.ClientException()
        if self.ctx.voice_client is None:
            raise discord.ClientException()
        if not isinstance(source, discord.AudioSource):
            raise TypeError()
        if not callable(after):
            raise TypeError()

        self._isPlaying = True
        self.source = source
        self._afterPlayFunc=after

    def stop(self):
        self._end_playing()
        self._calledStop = True

    def is_playing(self):
        return self._isPlaying

    def _end_playing(self):
        self._isPlaying = False
        self.source = None

        self._afterPlayFunc(None)
        
