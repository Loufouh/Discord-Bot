import discord

def emptyFunc():
    pass

class VoiceProtocol_dummy:
    def __init__(self, ctx):
        self.ctx = ctx
        self._isPlaying = False
        self.source = None
        self._afterPlayFunc=emptyFunc

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

    def is_playing(self):
        return self._isPlaying

    def _end_playing(self):
        self._isPlaying = False
        self.source = None

        self._afterPlayFunc()
        
