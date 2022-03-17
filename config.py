from typing import Tuple, List

BOT_PREFIX = "!"
COG_PATH = "./cogs"
DATA_PATH = "./resources/data.json"
BOT_ADMINS = [699802828356583435, 164788187296694274]

# Custom Emojis
CHECK_EMOJI: str = "<:check:655594481789173790>"
X_EMOJI: str = "<:xmark:655594482070454300>"

# Embed Colour Codes (Styling)
EMBED_COLOUR_STRD: hex = 0xffffff  # Old: 0xc2364e
EMBED_COLOUR_ERROR: hex = 0xf03f32
EMBED_COLOUR_SUCCESS: hex = 0x3ec966
EMBED_COLOUR_LOGS: hex = 0x6be2f2
EMBED_COLOUR_GOLD: hex = 0xd97f02
EMBED_COLOUR_INVIS: hex = 0x2f3136

# Auto Support Message
HOME_GUILD_ID: int = 831349828578574346
BOT_OWNER_ID: int = 699802828356583435


class JoinLeave:
    MESSAGE_CHANNEL_ID: int = 946227928600047737
    JOIN_COLOUR: hex = 0x3bb879
    LEAVE_COLOUR: hex = 0xd9092f


class LinkFilter:
    """
    Configuration for the URL filter

    """

    WHITELIST_PATH: str = "./resources/url_whitelist.txt"
    SEND_WARNING_DM: bool = True
    WARNING_MESSAGE: str = "Please **do not send links** to the Chromegle discord server! You sent `%s`. Thank you for your co-operation. :slight_smile:"
