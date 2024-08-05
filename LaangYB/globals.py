from fipper import Client, filters
from fipper.types import *

from pyLaang import Laang, CMD_HELP, DEVS
from pyLaang.pyrogram import eor
from pyLaang.dB.gban import add_gbanned, gbanned_users, is_gbanned, remove_gbanned
from pyLaang.decorator import listen


from . import *


# Define the owner ID and modify the function to check against it
OWNER_ID = 6144669103

def is_owner_or_admin(user_id):
    return user_id in DEVS or user_id == OWNER_ID


@Laang(["Cgban"], devs=True)
@Laang(["gban"], langs=True)
async def gban_user(client: Client, message: Message, _):
    if not is_owner_or_admin(message.from_user.id):
        return await message.reply("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    user_id, reason = await yins.extract_user_and_reason(message, sender_chat=True)
    Laang = await message.reply(_['p'])
    if not user_id:
        return await Laang.edit(_['err_user'])
    if user_id == client.me.id:
        return await Laang.edit(_['gban_1'])
    if user_id in DEVS:
        return await Laang.edit(_['Laang_2'])
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await Laang.edit(_['err_user'])

    if await is_gbanned(user.id):
        return await Laang.edit(_['gban_2'].format(user.mention))
    f_chats = await yins.get_ub_chats(client)
    if not f_chats:
        return await Laang.edit(_['gban_3'])
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    await add_gbanned(user.id)
    msg = _['gban_4'].format(user.mention, user.id)
    if reason:
        msg += _['admin_4'].format(reason)
    msg += _['gban_5'].format(done)
    await Laang.edit(msg)


@Laang(["Cungban"], devs=True)
@Laang(["ungban"], langs=True)
async def ungban_user(client: Client, message: Message, _):
    if not is_owner_or_admin(message.from_user.id):
        return await message.reply("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    user_id, reason = await yins.extract_user_and_reason(message, sender_chat=True)
    Laang = await message.reply(_['p'])
    if not user_id:
        return await Laang.edit(_['err_user'])
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await Laang.edit(_['err_user'])

    try:
        if not await is_gbanned(user.id):
            return await Laang.edit(_['gban_6'])
        ung_chats = await yins.get_ub_chats(client)
        if not ung_chats:
            return await Laang.edit(_['gban_3'])
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        await remove_gbanned(user.id)
        msg = _['gban_7'].format(user.mention, user.id)
        if reason:
            msg += _['admin_4'].format(reason)
        msg += _['gban_5'].format(done)
        await Laang.edit(msg)
    except Exception as e:
        await Laang.edit(_['err'].format(e))
        return


@Laang(["listgban"], langs=True)
async def gbanlist(client: Client, message: Message, _):
    if not is_owner_or_admin(message.from_user.id):
        return await message.reply("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    users = await gbanned_users()
    Laang = await eor(message, _['p'])
    if not users:
        return await Laang.edit(_['gban_8'])
    return await Laang.edit(_['gban_9'].format(users))


@listen(filters.incoming & filters.group)
async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if await is_gbanned(user_id):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    message.continue_propagation()


CMD_HELP.update(
    {"globals": (
        "globals",
        {
            "gban <reply/username/userid>": "Melakukan Global Banned Ke Semua Grup Dimana anda Sebagai Admin.",
            "ungban <reply/username/userid>": "Membatalkan Global Banned.",
            "listgban": "Menampilkan List Global Banned.",
        }
    )
    }
)