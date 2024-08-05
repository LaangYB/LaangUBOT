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

from random import choice

from pyLaang import Laang, CMD_HELP

from . import *


@Laang(["openai", "ai", "ask"], langs=True)
async def open_ai(_, message, YB):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>{choice(hndlr)}ai [question]</code> Pertanyaan untuk menggunakan OpenAI")
    question = yins.get_cmd(message)
    msg = await message.reply(YB["p"])
    try:
        ai_answer = await yins.ask_ai(question)
        await msg.edit(ai_answer)
    except BaseException as e:
        await msg.edit(YB["err"].format(e))


CMD_HELP.update(
    {"openai": (
        "openai",
        {
            "ai": "Berikan pertanyaan anda dan AI akan menjawabnya",
        }
        )
    }
)