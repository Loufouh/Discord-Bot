import discord

class FFmpegHandler:
    def create_audio_from_url(self, url):
        return discord.FFmpegPCMAudio(url)

