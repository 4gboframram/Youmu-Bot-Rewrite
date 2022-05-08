import asyncio
import random

import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_components import create_button, ButtonStyle, create_actionrow, wait_for_component

from src.constants import Constants
from src.embeds import YoumuEmbed
from .tictactoe import TTTGame


class RpsString(str):

    def __gt__(self, other):
        t = self.lower().strip(' ')

        if t == other:
            return 2  # tie

        elif any(
                [(t == "paper") and (other == "rock"),
                 (t == "rock") and (other == "scissors"),
                 (t == "scissors") and (other == "paper")]
        ):
            return 1
        elif t in ("rock", "paper", "scissors"):
            return 0
        else:
            return random.choice((0, 1, 2))  # If not rock, paper, or scissors, return a random result


class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='ttt', description="A game of Tic Tac Toe (Naughts and Crosses)",
                       )
    async def ttt(self, ctx, player: discord.Member):
        if player.id == ctx.author.id:
            await ctx.send("You can't challenge yourself!")
            return

        embed = YoumuEmbed(title='✉️Invitation!✉️',
                           description=f'{player.mention}, {ctx.author.mention} has challenged you to a game of ' +
                                       f'**Tic Tac Toe**.\n\nPress the button within the next minute to start the game.'
                                       + f'\n\n*Remember that if you don\'t accept, you might lose a friend~*',
                           color=0x53cc74)
        button = create_button(label='Accept Tic Tac Toe Invite', style=ButtonStyle.green, emoji='☑️')
        m = await ctx.send(embed=embed, components=[create_actionrow(button)])

        def check(res):
            return player.id == res.author.id and res.channel == ctx.channel

        try:
            res = await wait_for_component(self.bot, messages=m, check=check, timeout=60)
            if res.component.get('label') == 'Accept Tic Tac Toe Invite':
                game = TTTGame(self.bot, ctx, (ctx.author, player))
                await m.delete()
                await game.start()
        except asyncio.TimeoutError:
            button = create_actionrow(
                create_button(label='Expired Invite :(', style=ButtonStyle.red, emoji='❎', disabled=True))
            await m.edit(components=[button])

    @cog_ext.cog_slash(name="rps", description="Rock, Paper, Scissors... Shoot!")
    async def rps(self, ctx, choose: str) -> None:
        bot_choice = random.choice(["rock", "paper", "scissors"])
        choose = choose.lower()
        
        win_embed = YoumuEmbed(title="Rock, Paper, Scissors... Shoot!",
                               description=f"You chose **{choose.title()}**, " +
                                           f"I chose **{bot_choice.title()}**, I win", color=0xaa22cc)

        lose_embed = YoumuEmbed(title="Rock, Paper, Scissors... Shoot!",
                                description=f"You chose **{choose.title()}**, " +
                                            f"I chose **{bot_choice.title()}**, You win", color=0xaa22cc)

        tie_embed = YoumuEmbed(title="Rock, Paper, Scissors... Shoot!",
                               description=f"You chose **{choose.title()}**, " +
                                           f"I chose **{bot_choice.title()}**, Nobody wins", color=0xaa22cc)

        choose = RpsString(choose)

        if (choose > bot_choice) == 1:
            await ctx.send(embed=lose_embed)
        elif (choose > bot_choice) == 0:
            await ctx.send(embed=win_embed)
        else:
            await ctx.send(embed=tie_embed)
