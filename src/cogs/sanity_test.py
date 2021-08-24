from discord.ext import commands
from discord_slash import cog_ext
from src.constants import Constants
from random import choice

class SanityCheck(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", description="Pong?", )
    async def ping(self, ctx):
        await ctx.send(f'{choice(Constants.ping_messages)} ({self.bot.latency*1000:.2f}ms)')
