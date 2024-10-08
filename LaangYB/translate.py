from gpytranslate import Translator

from fipper import Client
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP
from pyLnnggg.pyrogram import eor

from . import *

@Laang(["tr", "tl", "translate"], langs=True)
async def translate(client: Client, message: Message, _):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        input_str = (
            message.text.split(None, 1)[1]
            if len(message.command) != 1
            else None
        )
        target = input_str or "id"
        text = (
            message.reply_to_message.text
            if message.reply_to_message.text
            else message.reply_to_message.caption
        )
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await eor(
                message,
                _['err'].format(str(err)),
            )
            return
    else:
        input_str = (
            message.text.split(None, 2)[1]
            if len(message.command) != 1
            else None
        )
        text = message.text.split(None, 2)[2]
        target = input_str or "id"
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await eor(
                message,
                _['err'].format(str(err)),
            )
            return
    await eor(
        message,
        _['translate'].format((await trl.detect(text)), target, tekstr.text)
    )


CMD_HELP.update(
    {"translate": (
        "translate",
        {
            "tr <text/reply>": "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa Indonesia)",
        }
    )
    }
)
