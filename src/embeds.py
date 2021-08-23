from discord import Embed


class YoumuEmbed(Embed):  # Creates a standard embed used by the bot
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_author(name="Youmu Bot",
                        icon_url='https://cdn.discordapp.com/avatars/847655832169480222/16c78890f9383ec318b4560675410120.webp?size=2048',
                        )
