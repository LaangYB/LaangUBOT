# ~ LaangUbot ~
# Copyright (C) 2024 @LaangYB
#
# This file is a part of < https://github.com/LaangYB/LaangUBOT >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUBOT/blob/main/LICENSE/>.
#
# FROM LaangUBOT <https://github.com/LaangYB/LaangUBOT>
# t.me/ybtraviss & t.me/ybtraviss


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper import Client, __version__ as fip_ver
from fipper.types import Message
from platform import python_version

from pyLaang import __version__, Laang_ver
from pyLaang import CMD_HELP, HOSTED_ON, tgbot
from pyLaang.decorator import Laang


from . import *


@Laang(["alive", "yins"])
async def aliveme(client: Client, message: Message):
    try:
        tgbot.me = await tgbot.get_me()
        results = await client.get_inline_bot_results(tgbot.me.username, f"alive")
        await message.reply_inline_bot_result(
            results.query_id,
            results.results[0].id,
            reply_to_message_id=yins.ReplyCheck(message),
        )
    except Exception:
        user = await client.get_me()
        output = (
            f"**Tʜᴇ [Laang Ubot](https://github.com/LaangYB/LaangUBOT)**\n\n"
            f"**{var.ALIVE_TEXT}**\n\n"
            f"╭✠╼━━━━━━━━━━━━━━━✠╮\n"
            f"≽ **Oᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
            f"≽ **Mᴏᴅᴜʟᴇs :** `{len(CMD_HELP)} Modules` \n"
            f"≽ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{python_version()}`\n"
            f"≽ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{fip_ver}`\n"
            f"≽ **Pʏ-Laaɴg Vᴇʀsɪᴏɴ :** `{__version__}`\n"
            f"≽ **Laaɴg Vᴇʀsɪᴏɴ :** `{Laang_ver}` [{HOSTED_ON}]\n"
            "╰✠╼━━━━━━━━━━━━━━━✠╯\n\n"
        )
        await message.delete()
        await message.reply_text(
            text=output,
            disable_web_page_preview=True,
        )


CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Chech Your Userbot.",
        }
    )
    }
)