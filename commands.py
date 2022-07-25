from Bot import get_bot

bot = get_bot()

@bot.command(name='hello')
async def _hello(ctx):
    await ctx.send('Hello {}'.format(ctx.author))

