import aiohttp
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow

from src.constants import Constants
from src.embeds import YoumuEmbed


class Others(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='inspire', description="Feeling sad? Try this!", guild_ids=Constants.test_guild_id)
    async def inspire(self, ctx):
        try:
            url = 'http://inspirobot.me/api?generate=true'
            params = {'generate': 'true'}
            async with aiohttp.ClientSession() as s:
                async with s.get(url, params=params) as response:
                    image = await response.text()
            embed = YoumuEmbed(title='Inspiration.jpg', colour=0x53cc74)
            embed.set_image(url=image)

            await ctx.send(embed=embed)

        except aiohttp.ClientError:
            await ctx.send('Inspirobot is broken, there is no reason to live.')

    @cog_ext.cog_slash(name='help', description='View the help and documentation for the bot',
                       guild_ids=Constants.test_guild_id)
    async def help(self, ctx):
        buttons = [
            create_button(style=ButtonStyle.URL, label="Github Repo",
                          url="https://github.com/4gboframram/Youmu-Bot-Rewrite")
        ]
        action_row = create_actionrow(*buttons)
        embed = YoumuEmbed(title="Help?",
                           description="Click the button to go the github repo that contains the documentation: ",
                           colour=0x11ff11)
        await ctx.send(embed=embed, components=[action_row])
