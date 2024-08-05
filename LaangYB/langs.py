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

from fipper import Client
from fipper.types import Message

from pyLaang import Laang, CMD_HELP
from pyLaang.Clients.client import tgbot

from . import *


@Laang(["lang"], langs=True)
async def set_lang(client: Client, message: Message, _):
    try:
        tgbot.me = await tgbot.get_me()
        results = await client.get_inline_bot_results(tgbot.me.username, f"langs_{client.me.id}")
        await message.reply_inline_bot_result(
            results.query_id,
            results.results[0].id,
            reply_to_message_id=yins.ReplyCheck(message),
        )
    except BaseException as e:
        await message.reply(_["err"].format(e))


CMD_HELP.update(
    {"langs": (
        "langs",
        {
            "lang": "Pilih bahasa yang ingin anda gunakan.",
        }
        )
    }
)