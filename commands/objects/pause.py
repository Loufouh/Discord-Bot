from commands.exceptions.exceptions import AlreadyPausedException

from message_sender import MessageSender

class PauseCommand:
    async def execute(self, ctx):
        self.messageSender = MessageSender(ctx)

        try:
            await self.try_to_execute(ctx)
        except AlreadyPausedException:
            await self.messageSender.send('C\'est déjà en pause')
    
    async def try_to_execute(self, ctx):
        if ctx.voice_client.is_paused():
            raise AlreadyPausedException()

        ctx.voice_client.pause()
        await self.messageSender.send('Je mets en pause')

