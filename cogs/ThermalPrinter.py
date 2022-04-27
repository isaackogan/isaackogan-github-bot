import datetime
from typing import Optional

import discord
from discord import Message, PartialEmoji
from discord.ext import commands
from dislash import ActionRow, Button, ButtonStyle, MessageInteraction

import config
from bot import ChromegleSupport

from modules.TagItem import TagItem
from modules.BotUtil import BotUtil


class ThermalPrinter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, interaction: MessageInteraction):

        if int(interaction.guild_id) != config.HOME_GUILD_ID:
            return

        schema: Optional[str] = {
            "_getPayPal": (
                "paypal@isaackogan.com\n\n"
                "PLEASE make sure you select 'No Address Required' if you choose to send via business."
            ),
            "_getBTC": "bc1qdceyw3ekmz5ehdrjukn49dgj79npgkwtmkk8sn",
            "_getETH": "0x17C200a5858D6CFE698A1eb31627d504ae0582e3"
        }.get(interaction.button.id)

        if schema is None:
            return

        await interaction.reply(content=schema, ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        # Must be in ticket category
        if str(message.channel.category.id) != "959287400327168000":
            return

        # Check for keyword
        if "printer magic" not in message.content.lower():
            return

        # Create embed
        embed = discord.Embed(
            title="Thanks for your interest in Thermal Printing! :printer: ",
            colour=config.EMBED_COLOUR_STRD,
            description=(
                "The product is provided without warranty. Support is provided, but Python knowledge is **required** for "
                "advanced usage/customization.\n\n"
                "Purchasing the `TikTokPrinter` library grants you access to all future releases "
                "of the product, and, private channels relating to developing around the library.\n\n"
                "The cost for this library is `$50 USD`. This is unbelievably cheap. Simply [**check out**](https://github.com/isaackogan/TikTokprinter) the "
                "*extensive* feature list, maintained docs, and robust examples on the GitHub page.\n\n"
                "Payments are available through `PayPal/BTC/ETH` and are in USD. Delivery time can vary based on when a support agent is available. "
                "Items that have been paid for will be delivered on average within `0-3 hours`, at maximum within 24 hours.\n\n"
                f"To start a transaction, click one of the buttons below to get your desired payment medium. Once you've paid, "
                f"**you must** ping <@{config.BOT_OWNER_ID}> to receive library access."
            )
        )

        row = ActionRow(
            Button(
                style=ButtonStyle.grey,
                label="PayPal Address",
                custom_id="_getPayPal",
                emoji="<:paypal:968689967817695252>"
            ),
            Button(
                style=ButtonStyle.grey,
                label="Bitcoin Address",
                custom_id="_getBTC",
                emoji="<:bitcoin:968690230444044318>"
            ),
            Button(
                style=ButtonStyle.grey,
                label="Etherium Address",
                custom_id="_getETH",
                emoji="<:etherium:968690069823193118>"
            )
        )

        await message.reply(embed=embed, mention_author=False, components=[row])


def setup(bot):
    bot.add_cog(ThermalPrinter(bot))
