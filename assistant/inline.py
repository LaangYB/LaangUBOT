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

import time

from platform import python_version
from datetime import datetime

from fipper import __version__ as fip_ver, Client
from fipper.types import *

from config import *

from pyLaang import CMD_HELP, HOSTED_ON, StartTime, __version__, Laang_ver, hndlr
from pyLaang.assistant import inline

from . import *


def help_string():
    text = f"""
<b>Help Module:</b>
    <b>Prefixes:</b> <code>{hndlr}</code>
    <b>Plugin:</b> <code>{len(CMD_HELP)}</code>
"""

    return text


def update_string():
    teks = f'''
<b>Tersedia Pembaruan Untuk [{branch}]</b>

<b>•</b> Klik Update Untuk Memperbarui [{branch}]
<b>•</b> Klik Changelog Untuk Melihat Pembaruan
'''
    
    return teks


def alive_string():
    output = f'''
<b> Laang UBOT</b>
<b>{var.ALIVE_TEXT}</b>
<b>╭✠╼━━━━━━━━━━━━━━━✠╮</b>
≽ <b>Mᴏᴅᴜʟᴇs :</b> <code>{len(CMD_HELP)} Modules</code>
≽ <b>Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :</b> <code>{python_version()}</code>
≽ <b>Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :</b> <code>{fip_ver}</code>
≽ <b>Pʏ-Laang Vᴇʀsɪᴏɴ :</b> <code>{__version__}</code>
≽ <b>Laang Vᴇʀsɪᴏɴ :</b> <code>{Laang_ver}</code> [{HOSTED_ON}]
╰✠╼━━━━━━━━━━━━━━━✠╯
    '''
    return output


@inline(pattern="help")
async def inline_result(_, inline_query):
    rslts= await yins.inline_help(help_string())
    await inline_query.answer(
        rslts,
        cache_time=0
    )


@inline(pattern="paste", client_only=True)
async def inline_result(_, iq):
    query = iq.query
    ok = query.split("-")[1]
    rslts=[
        (
            InlineQueryResultArticle(
                title="Paste Laang UBOT!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="• SpaceBin •",
                                url=f"https://spaceb.in/{ok}",
                            ),
                            InlineKeyboardButton(
                                text="• Raw •",
                                url=f"https://spaceb.in/api/v1/documents/{ok}/raw",
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent("Pasted to Spacebin 🌌"),
            )
        )
    ]
    await iq.answer(
        rslts,
        cache_time=0
    )


@inline(pattern="alive", client_only=True)
async def inline_result(_: Client, iq):
    aliv = await yins.inline_alive(alive_string())
    await iq.answer(
        aliv,
        cache_time=0
    )



@inline(pattern="ping", client_only=True)
async def inline_result(_: Client, iq):
    start = datetime.now()
    uptime = await yins.get_readable_time((time.time() - StartTime))
    time.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    out_ping = (
        f"<b>✧ Laang UBOT ✧</b>\n\n"
        f"<b>✧ Pɪɴɢᴇʀ :</b> <code>{duration}ms</code>\n"
        f"<b>✧ Uᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>"
    )
    ping_result = [
        (
            InlineQueryResultArticle(
                title="Ping Laang UBOT!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="• Help •",
                                callback_data="plugins-tab",
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent(out_ping),
            )
        )
    ]
    await iq.answer(
        ping_result,
        cache_time=0,
    )



@inline(pattern='in_update', client_only=True)
async def inline_update(client, iq):
    query = iq.query
    update_results = [
        (
            InlineQueryResultArticle(
                title='Update Laang UBOT!',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text='• Update •',
                                callback_data='update_now',
                            ),
                            InlineKeyboardButton(
                                text='• Changelog •',
                                callback_data='changelog',
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent(update_string()),
            )
        )
    ]
    await iq.answer(
        update_results,
        cache_time=0,
    )


@inline(pattern='pmpermit', client_only=True)
async def inline_pmpermit(_, iq):
    query = iq.query
    ids = query.split("_")[1]
    user_ids = query.split("_")[2]
    xnxx = await yins.inline_pmpermit(ids, user_ids)
    await iq.answer(
        xnxx,
        cache_time=0,
    )


@inline(pattern='pin')
async def inline_update(client, iq):
    query = iq.query
    ok = query.split("_")[1]
    update_results = [
        (
            InlineQueryResultArticle(
                title='Pinned Laang UBOT!',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text='• Cek Pinned •',
                                url=f'{ok}',
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent(f'\nPesan Berhasil di sematkan tod!!!'),
            )
        )
    ]
    await iq.answer(
        update_results,
        cache_time=0,
    )


@inline(pattern='langs', client_only=True, langs=True)
async def inline_lang(client, iq, _):
    text, button = await yins.inline_languages(_)
    update_results = [
        (
            InlineQueryResultArticle(
                title='Lang Laang UBOT!',
                reply_markup=InlineKeyboardMarkup(button),
                input_message_content=InputTextMessageContent(text),
            )
        )
    ]
    await iq.answer(
        update_results,
        cache_time=0,
    )