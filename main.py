import os

from discord.ext import commands
from discord_slash import SlashCommand
from src.cogs import random_fun, sanity_test, background
from src.cogs import other
from src.cogs.sauces.characters import Characters
from src.cogs.games import Games
from src.cogs.spellcard import Spellcard

TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix=',', help_command=None)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(bot.user.name, "has connected to discord")
    print("Starting background tasks")
    bg = background.BackgroundTasks(bot)
    bg.change_status.start()


bot.add_cog(random_fun.RandomFun(bot))
bot.add_cog(sanity_test.SanityCheck(bot))
bot.add_cog(Characters(bot))
bot.add_cog(other.Others(bot))
bot.add_cog(Games(bot))
bot.add_cog(Spellcard(bot))
# bot.add_cog(hentai.Hentai(bot))
# bot.add_cog(background.BackgroundTasks(bot))

bot.run(TOKEN)
