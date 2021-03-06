import discord
from discord.ext import commands, tasks
from src.constants import Constants
from random import choice


class BackgroundTasks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.previous_presence = None

    @tasks.loop(hours=1)
    async def change_status(self):
        print("[LOG] Changing Status...")
        chosen_presence = choice(Constants.presences)
        while chosen_presence == self.previous_presence:
            chosen_presence = choice(Constants.presences)

        await self.bot.change_presence(activity=discord.Game(chosen_presence))
        self.previous_presence = chosen_presence
        print("[LOG] Changed Status Successfully!")
