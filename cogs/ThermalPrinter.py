import datetime

import discord
from discord.ext import commands

import config

from modules.TagItem import TagItem
from modules.BotUtil import BotUtil


class ThermalPrinter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if not (
            any(word in str(message.content) for word in ["want", "make", "help", "start", "learn", "please"])
            and
            any(word in str(message.content) for word in ["thermal", "receipt", "printer"])
        ):
            return

        embed = discord.Embed(
            title="So, you want a printer...",
            colour=config.EMBED_COLOUR_ERROR,
            description=(
                "Unfortunately, we **can't provide support** for projects involving thermal printing. "
                "The code required is super specific to your printer's system, so we cannot help you further. "
                "If you would like to set up thermal printing, try [searching on Google](https://lmgtfy.app/?q=thermal+printer+python+youtube) for a tutorial that uses your specific printer."
            )
        ).set_footer(
            text="This message will self-destruct in 60 seconds, so read it quickly!"
        )

        await message.reply(embed=embed, delete_after=60, mention_author=False)



def setup(bot):
    bot.add_cog(ThermalPrinter(bot))
