from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" Sᴛᴀʀᴛ Gᴇɴʀᴀᴛɪɴɢ ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/ZenBotX")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="https://t.me/NoobZen")],
    ]

    START = """
Hᴇʏ {}
ᴛʜɪs ɪs {}  

ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ,  
1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ 
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ  

ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?

ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. 
ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

**__Pᴏᴡᴇʀᴇᴅ ʙʏ__** @ZenBotX
    """

    HELP = """
✨ **ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴛʜɪs ʙᴏᴛ** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process

**__Pᴏᴡᴇʀᴇᴅ ʙʏ__** @ZenBotX
"""

    ABOUT = """
**Aʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

Tᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ Pʏʀᴏɢʀᴀᴍ & Tᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @ZenBotX

**Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/PyAaditya/StringSession)

**Fʀᴀᴍᴇᴡᴏʀᴋ** : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

**Lᴀɴɢᴜᴀɢᴇ** : [ᴘʏᴛʜᴏɴ](https://www.python.org)

**Dᴇᴠᴇʟᴏᴘᴇʀ** : @NoobZen
    """
