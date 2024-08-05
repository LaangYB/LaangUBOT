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

import os
import re
import random

import aiofiles
from fipper import Client
from fipper.types import Message

from pyLaang import Laang, CMD_HELP, tgbot
from pyLaang.pyrogram import eor

from . import *

# List of allowed user IDs
ALLOWED_USER_IDS = list(range(1, 10))

def is_allowed_user(user_id):
    return user_id in ALLOWED_USER_IDS

@Laang(["paste", "pst"], langs=True)
async def paste_func(client: Client, message: Message, _):
    if not is_allowed_user(message.from_user.id):
        return await message.reply("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    if not message.reply_to_message:
        return await eor(message, _['reply'])
    r = message.reply_to_message
    if not r.text and not r.document:
        return await eor(message, _['paste_1'])
    m = await eor(message, _['p'])
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit(_['paste_2'])
        pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")
        if not pattern.search(r.document.mime_type):
            return await m.edit(_['paste_3'])
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    
    # Generate a unique key between 1 and 9
    key = random.randint(1, 9)
    link = f"https://spaceb.in/{key}"
    raw = f"https://spaceb.in/api/v1/documents/{key}/raw"
    try:
        if tgbot:
            try:
                tgbot.me = await tgbot.get_me()
                results = await client.get_inline_bot_results(tgbot.me.username, f"paste-{key}")
                await message.reply_inline_bot_result(
                    results.query_id,
                    results.results[0].id,
                    reply_to_message_id=yins.ReplyCheck(message),
                )
            except BaseException as e:
                await m.edit(e)
        else:
            await message.reply_photo(
                photo=link,
                quote=False,
                caption=_['paste_4'].format(link, raw),
            )
        await m.delete()
    except BaseException as e:
        await m.edit(_['err'].format(e))

CMD_HELP.update(
    {"paste": (
        "paste",
        {
            "paste": "Untuk Menyimpan text ke ke layanan pastebin.",
        }
    )
    }
)
