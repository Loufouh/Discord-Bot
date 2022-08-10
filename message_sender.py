
class MessageSender:
    def __init__(self, ctx):
        self.ctx = ctx
        self.mentionningActivated = True

    async def send(self, message):
        if self.mentionningActivated:
            message += ' ' + self.ctx.author.mention

        await self.ctx.send(message)

