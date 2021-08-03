import os

from discord.ext import commands
from discord_slash import SlashCommand

from cogs import random_fun, sanity_test, background, other
from cogs.sauces.characters import Characters

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
# bot.add_cog(hentai.Hentai(bot))
# bot.add_cog(background.BackgroundTasks(bot))

bot.run(TOKEN)
