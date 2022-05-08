import difflib
import random
from random import randint

import discord.errors
from discord.ext import commands
from discord_slash import cog_ext
from retry import retry

from .finder import char, join_tags
from src.constants import Constants, CommandList
from src.embeds import YoumuEmbed

character_name_list = [i.name for i in CommandList.character_list]
# alias_commands = [i for i in character_list if i[1] != "placeholder description"]


class Characters(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        for command in CommandList.alias_commands:
            self.make_command(*command)
            print("[LOG]: Registed", repr(command[0]), "with description:", repr(command[1]))

    def make_command(self, name, description, tag, score):

        @cog_ext.cog_slash(name=name, description=description)
        @retry(exceptions=discord.errors.NotFound, delay=2, tries=4)
        async def char_command(self, ctx, *, args=None):
            await ctx.defer()
            if args and "--desc" in args:
                await ctx.send(f'{name.title()}: {description}')
                return
            if score:
                score_rng = randint(0, 5)
                await char(ctx, tag + f'+score:>={score_rng}', args=args)
                return
            await char(ctx, tag, args=args)

        setattr(self, name, char_command)

    @cog_ext.cog_slash(name='c',
                       description="The command used for searching artworks of all 146 characters",)
    @retry(exceptions=discord.errors.NotFound, tries=4, delay=2)
    async def c(self, ctx, name, *, args=None):
        _name = name.lower().strip()

        for i in CommandList.character_list:
            if _name == i.name:
                if args and "--desc" in args:
                    await ctx.send(f'{name.title()}: {i.description}')
                    return
                if not i.use_score:
                    await char(ctx, i.tag, args=args)
                    return
                await char(ctx, i.tag + f'+score:>={random.randint(0, 5)}', args=args)
                return
        try:
            await ctx.send(embed=YoumuEmbed(title='Woops!',
                                            description=f"**{name.title()}** is not a character on my list! " +
                                                        f"Perhaps did you mean **{difflib.get_close_matches(name.lower(), character_name_list)[0].title()}**?",
                                            color=0xff0000))
        except IndexError:
            await ctx.send(embed=YoumuEmbed(title='Woops!',
                                            description=f"**{name.title()}** is not a character on my list!",
                                            color=0xff0000))

    @cog_ext.cog_slash(name='char_list', description="I'll dm you the list of characters")
    async def li(self, ctx):
        await ctx.author.send(embed=YoumuEmbed(title="List of Characters",
                                               description='\n'.join(
                                                   [character.name.title() for character in
                                                    CommandList.character_list]),
                                               color=0xfcdeae))
        await ctx.send('Check your dms ;)')

    @cog_ext.cog_slash(name="tag", description="Search for artworks with given tags")
    async def tag(self, ctx, *, tags, args=None):
        await ctx.defer()
        tags = tags.split()
        tags = join_tags(tags)
        await char(ctx, tags, args=args)
