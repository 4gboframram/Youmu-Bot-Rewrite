import hashlib
import random

from discord.ext import commands
from discord_slash import cog_ext

from src.constants import Constants
from src.embeds import YoumuEmbed


class RandomFun(commands.Cog):
    """
    Adds the following commands:
    /rate
    /percent
    """

    def __init__(self, bot):
        self.bot = bot

    @property
    def embed_color(self):
        return 0xcc00ff

    @classmethod
    def rng(cls, thing: str, upper: int) -> int:
        digest = hashlib.md5(thing.encode("utf8")).digest()
        gen = random.Random(digest)
        return gen.randint(0, upper)

    @cog_ext.cog_slash(name="rate", description="What would I rate this thing out of 10?")
    async def rate(self, ctx, *, thing: str) -> None:
        h = RandomFun.rng(thing, 10)
        embed = YoumuEmbed(title='Rate',
                           description=f"I would rate *{thing}* {'an' if h == 8 else 'a'} {h} out of 10",
                           colour=self.embed_color)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="percent", description="What percent this thing are you?")
    async def percent(self, ctx, *, thing: str) -> None:
        h = RandomFun.rng(str(ctx.author.id) + thing, 100)
        embed = YoumuEmbed(title="You are...",
                           description=f"{ctx.author.mention}, you are {h}% *{thing}*",
                           colour=self.embed_color)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="ship", description="The love boat sets sail...")
    async def ship(self, ctx, thing_1: str, thing_2: str = None) -> None:
        if not thing_2:
            thing_2 = ctx.author.mention
        ship_percent = (
                               int.from_bytes(hashlib.md5(thing_1.encode("utf8")).digest(), 'big') +
                               int.from_bytes(hashlib.md5(thing_2.encode("utf8")).digest(), 'big')
                       ) % 101
        if any("692981485975633950" in thing for thing in (thing_1, thing_2)):
          ship_percent = 101
        
        ship_compatibility = "Perfect" if 90 < ship_percent <= 100 else "Very Good" if 80 < ship_percent <= 90 else \
            "Decent" if 70 < ship_percent <= 80 else "Slightly Above Average" if 50 < ship_percent <= 70 else \
               "Slightly Below Average" if 40 < ship_percent <= 50 else "Horrible"

        bar_len = 15
        bar = int(bar_len * ship_percent / 100) * '💚' + (bar_len - int(bar_len * ship_percent / 100)) * '🖤'

        embed = YoumuEmbed(title="The Love Boat has Sailed!",
                           description=f"**{thing_1}** and **{thing_2}** are **{ship_percent}%** compatible!",
                           colour=self.embed_color)
        embed.add_field(name=f"**{ship_percent}%**", value=f'{bar}')
        embed.set_footer(text=f"Compatibility: {ship_compatibility}!")
        await ctx.send(embed=embed)
