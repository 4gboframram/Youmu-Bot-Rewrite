from pathlib import Path
import os
from discord.ext import commands
from src.constants import Constants
from random import randint
from discord_slash import cog_ext
from src.markov import Markov
import string


class Spellcard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open(str(Path(os.getcwd(), "assets", "spellcards.txt"))) as f:
            data = f.read().lower().replace('-', ' ').replace('"', ' ')
            data = filter(lambda x: x in string.ascii_lowercase + string.digits + ' %', data)
            data = ''.join(data)
            self.markov = Markov(data.split(' '))
            self.markov.train()

    def generate_spellcard(self):
        while True:
            result = list(self.markov.generate(word_count=randint(4, 8)))
            if "sign" in result:
                i = result.index("sign")
                if i < (len(result) - 2) and i != 0 and result.count('sign') == 1:
                    result[i+1] = '｢' + result[i+1]
                    result[-1] += '｣'
                    break
            """else:
                return '"' + ' '.join(result).replace('\n', ' ').title() + '"'"""

        return ' '.join(result).title().replace('｢ ', '｢')

    @cog_ext.cog_slash(name="spellcard", description="Create a random spellcard name?", )
    async def spellcard(self, ctx):
        await ctx.send(self.generate_spellcard())


