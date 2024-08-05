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
from fipper.errors import PeerIdInvalid
from fipper.types import Message

from pyLaang import Laang, CMD_HELP
from pyLaang.pyrogram import eod, eor

from . import *


@Laang(["whois", "info"], langs=True)
async def check_user(client: Client, msg: Message, _):
    xx = await eor(msg, _['p'])
    try:
        users = msg.text.split(" ", 1)[1]
        try:
            target = await client.get_users(users)
        except PeerIdInvalid:
            return await eod(xx, _["err_user"])
        name = target.first_name + " " + target.last_name if target.last_name else target.first_name
        uname = f"@{target.username}" if target.username else "⊗"
        out_str = (
            f"""
**⇒ Informasi Pengguna ⇐**

**Name:** `{name}`
**Username:** {uname}
**User ID:** `{target.id}`
**User Prem:** `{target.is_premium}`
**Profil:** [{name}](tg://user?id={target.id})
"""
        )
        await xx.edit(out_str)
    except BaseException as ex:
        return await eod(xx, ex)


CMD_HELP.update(
    {"info": (
        "info",
        {
            "info <id/username>" : "Dapatkan Informasi Pengguna.",
        }
    )
        
    }
)