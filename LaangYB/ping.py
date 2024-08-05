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

from pyLaang import CMD_HELP, tgbot
from pyLaang.decorator import Laang

from . import *


@Laang(["ping"], langs=True)
async def pingme(client: Client, message: Message, _):
    if tgbot:
        try:
            xnxx = await message.reply("<b>✧</b>")
            await xnxx.edit("<b>✧✧</b>")
            await xnxx.edit("<b>✧✧✧</b>")
            await xnxx.edit("<b>✧✧✧✧</b>")
            await xnxx.edit("<b>✧✧✧✧✧</b>")
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, "ping")
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(message),
            )
            await xnxx.delete()
        except BaseException as e:
            await eod(xnxx, _['err'].format(e))


CMD_HELP.update(
    {"ping": (
        "ping",
        {
            "ping": "Check Ping Your Bot.",
        }
    )
    }
)