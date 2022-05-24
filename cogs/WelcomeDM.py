import datetime
from typing import Optional

import discord
from discord import Message, PartialEmoji, Member, TextChannel
from discord.ext import commands
from dislash import ActionRow, Button, ButtonStyle

import config


class WelcomeDM(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):

        # Create embed
        embed = discord.Embed(
            title="Welcome to the Eulerstream Discord! :printer:",
            colour=config.EMBED_COLOUR_STRD,
            description=(
                "_ _\n"
                "For thermal printing inquiries, create a ticket in the <#978699673827155979> channel. A representative will be with you as soon as possible."
                "\n\n_ _"
            )
        )

        embed.set_thumbnail(url=self.bot.get_guild(config.HOME_GUILD_ID).icon_url)

        row = ActionRow(
            Button(
                style=ButtonStyle.link,
                label="Create Ticket",
                url="https://ptb.discord.com/channels/831349828578574346/978699673827155979/978699674615709766"
            )
        )

        try:
            dm: TextChannel = await member.create_dm()
            await dm.send(embed=embed, mention_author=False, components=[row])
        except:
            pass


def setup(bot):
    bot.add_cog(WelcomeDM(bot))
