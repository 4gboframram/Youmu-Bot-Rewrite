import asyncio
from typing import Union

import discord
import discord_slash
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, spread_to_rows, wait_for_component
from retry import retry
from src.embeds import YoumuEmbed

class Tile:
    def __init__(self, owner: Union[discord.Member, None] = None):
        self.owner = owner

    def __repr__(self):
        if self.owner is None:
            return 'empty'
        return self.owner.name

    def __eq__(self, other):
        return self.owner == other.owner


class TTTGame:
    def __init__(self, bot, ctx, players: tuple):
        self.bot = bot
        self.channel = None
        self.ctx = ctx

        self.players = players
        self.players_dynamic = list(self.players)  # used for turn order to swap the players
        self.state = [Tile()] * 9

        self.buttons = [create_button(emoji='⬛', custom_id=str(i + 1), style=ButtonStyle.gray) for i in
                        range(9)]  # id zero tends to be wonky
        self.buttons_inline = None  # it's annoying to work with a multidimensional matrix
        # so we have a flat version and a the version that will be used on the bot
        self.turn_owner = self.players[0]
        self.message = None

    def update_inline_buttons(self):
        self.buttons_inline = spread_to_rows(*self.buttons, max_in_row=3)

    async def start(self):
        self.update_inline_buttons()
        self.message = await self.ctx.send(content=f'Game has started, {self.players[0].mention}, your turn first',
                                           components=self.buttons_inline)
        await self.take_turn(self.turn_owner)

    def check_win(self):
        state = self.state

        winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        player_1_owned = [i for i in range(9) if self.state[i].owner == self.players[0]]
        player_2_owned = [i for i in range(9) if self.state[i].owner == self.players[1]]
        for combo in winning_combos:
            if set(combo).issubset(set(player_1_owned)) or set(combo).issubset(set(player_2_owned)):
                return True
        if all([tile.owner for tile in state]):  # check for full board
            return None
        return False

    async def take_turn(self, player):
        def check(res):
            return res.author_id == player.id and res.channel_id == self.ctx.channel.id \
                   and res.component.get('label') is None

        try:
            res = await wait_for_component(self.bot, check=check, messages=self.message, timeout=600)

            button_pos = int(res.component.get('custom_id'))

            await res.defer(edit_origin=True)
            player_ = res.author
            await self.process_turn(player_, button_pos - 1, res)
        except asyncio.TimeoutError:
            await self.ctx.send(
                "Game ends in a draw because you were taking too long. I have to go cook dinner for Yuyuko-sama now")
            self.buttons = [
                create_button(custom_id=button.get('custom_id'), emoji=button.get('emoji'), style=button.get('style'),
                              disabled=True) for button in
                self.buttons]
            self.update_inline_buttons()
            await self.message.edit(components=self.buttons_inline)

    @retry(exceptions=discord.errors.NotFound, delay=2, tries=4)
    async def process_turn(self, player: discord.Member, position: int, res: discord_slash.ComponentContext):

        self.state[position] = Tile(player)
        if player == self.players[0]:
            self.buttons[position] = create_button(style=ButtonStyle.blue, emoji='⬛',
                                                   custom_id=self.buttons[position].get('custom_id'),
                                                   disabled=True)
        else:
            self.buttons[position] = create_button(style=ButtonStyle.red, emoji='⬛',
                                                   custom_id=self.buttons[position].get('custom_id'),
                                                   disabled=True)
        self.update_inline_buttons()
        await res.origin_message.edit(components=self.buttons_inline)

        win = self.check_win()
        if win:
            embed = YoumuEmbed(title='Winner!',
                                  description=f'{player.mention}, you win this game of **Tic Tac Toe**', color=0x53cc74)

            self.buttons = [
                create_button(custom_id=button.get('custom_id'), emoji=button.get('emoji'), style=button.get('style'),
                              disabled=True) for button in
                self.buttons]
            self.update_inline_buttons()
            await self.message.edit(content='Game Over', embed=embed, components=self.buttons_inline)
            return
        if win is None:
            embed = YoumuEmbed(title='Draw', description=f'Nobody wins this game of **Tic Tac Toe**', color=0x53cc74)

            self.buttons = [
                create_button(custom_id=button.get('custom_id'), emoji=button.get('emoji'), style=button.get('style'),
                              disabled=True) for button in
                self.buttons]
            self.update_inline_buttons()
            await self.message.edit(content='Game Over!', embed=embed, components=self.buttons_inline)
            return
        self.players_dynamic.reverse()
        self.turn_owner = self.players_dynamic[0]

        await self.message.edit(content=f'{self.turn_owner.mention}, your turn')

        await self.take_turn(self.turn_owner)
