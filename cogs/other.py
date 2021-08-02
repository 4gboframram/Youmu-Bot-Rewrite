import aiohttp
import requests
from discord.ext import commands
from discord_slash import cog_ext

from .embeds import YoumuEmbed


class Others(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='inspire')
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
