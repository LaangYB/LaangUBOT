import asyncio
from fipper import Client, enums
from fipper.errors import ChatAdminRequired, UserCreator
from fipper.types import ChatPermissions, ChatPrivileges, Message

from pyLnnggg import Laang, CMD_HELP, DEVS, tgbot
from pyLnnggg.pyrogram import eor

from . import yins  # Assuming `yins` is a module you have

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@Laang(
    ["setchatphoto", "setgpic"],
    langs=True,
)
async def set_chat_photo(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        if message.reply_to_message and message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
        else:
            await message.edit_text(_["admin_1"])

@Laang(["Cban"], devs=True)
@Laang(["ban"], langs=True)
async def member_ban(client: Client, message: Message, _):
    me = client.me
    if await yins.CheckAdmin(client, message):
        Laang = await eor(message, _["p"])
        user_id, reason = await yins.extract_user_and_reason(message, sender_chat=True)
        if not user_id:
            return await Laang.edit(_["err_user"])
        if user_id == client.me.id:
            return await Laang.edit(_["admin_2"])
        if user_id in DEVS:
            return await Laang.edit(_["laang_2"])
        try:
            mention = (await client.get_users(user_id)).mention
        except IndexError:
            mention = (
                message.reply_to_message.sender_chat.title
                if message.reply_to_message
                else "Anon"
            )
        msg = _["admin_3"].format(mention, me.mention)
        if message.command[0][0] == "d":
            await message.reply_to_message.delete()
        if reason:
            msg += _["admin_4"].format(reason)
        try:
            await message.chat.ban_member(user_id)
            await Laang.edit(msg)
        except ChatAdminRequired:
            await Laang.edit(_["admin_5"])
        except UserCreator:
            await Laang.edit(_["admin_6"])

@Laang(["Cunban"], devs=True)
@Laang(["unban"], langs=True)
async def member_unban(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        Laang = await eor(message, _["p"])
        reply = message.reply_to_message
        if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
            return await Laang.edit(_["admin_7"])

        if len(message.command) == 2:
            user = message.text.split(None, 1)[1]
        elif len(message.command) == 1 and reply:
            user = reply.from_user.id
        else:
            return await Laang.edit(_["admin_8"])
        await message.chat.unban_member(user)
        umention = (await client.get_users(user)).mention
        await Laang.edit(_["admin_9"].format(umention))

@Laang(["gpin", "gunpin"], devs=True)
@Laang(["pin", "unpin"], langs=True)
async def pin_message(client: Client, message: Message, _):
    if not message.reply_to_message:
        return await eor(message, _["reply"])
    r = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
        try:
            if message.command[0][0] == "u":
                await r.unpin()
                return await eor(message, _["admin_10"])
            await r.pin(disable_notification=True)
            await eor(message, _["admin_11"])
        except Exception:
            pass
    if await yins.CheckAdmin(client, message):
        LaangYB = await eor(message, _["p"])
        try:
            if message.command[0][0] == "u":
                await r.unpin()
                return await LaangYB.edit(_["admin_12"])
            await r.pin(disable_notification=True)
            try:
                tgbot.me = await tgbot.get_me()
                results = await client.get_inline_bot_results(tgbot.me.username, f"pin_{r.link}")
                await message.reply_inline_bot_result(
                    results.query_id,
                    results.results[0].id,
                    reply_to_message_id=yins.ReplyCheck(message),
                )
                await LaangYB.delete()
            except Exception as e:
                await LaangYB.edit(_["err"].format(e))
        except ChatAdminRequired:
            await LaangYB.edit(_["admin_5"])

@Laang(["Cmute"], devs=True)
@Laang(["mute"], langs=True)
async def mute(client: Client, message: Message, _):
    me = client.me
    if await yins.CheckAdmin(client, message):
        Laang = await eor(message, _["p"])
        user_id, reason = await yins.extract_user_and_reason(message)
        if not user_id:
            return await Laang.edit(_["err_user"])
        if user_id == client.me.id:
            return await Laang.edit(_["admin_12"])
        if user_id in DEVS:
            return await Laang.edit(_["laang_2"])
        mention = (await client.get_users(user_id)).mention
        msg = _["admin_13"].format(mention, me.mention)
        if reason:
            msg += _['admin_4'].format(reason)
        try:
            await message.chat.restrict_member(user_id, permissions=ChatPermissions())
            await Laang.edit(msg)
        except ChatAdminRequired:
            await Laang.edit(_["admin_5"])
        except UserCreator:
            await Laang.edit(_["admin_6"])

@Laang(["Cunmute"], devs=True)
@Laang(["unmute"], langs=True)
async def unmute(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        Laang = await eor(message, _["p"])
        user_id = await yins.extract_user(message)
        if not user_id:
            return await Laang.edit(_["err_user"])
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        umention = (await client.get_users(user_id)).mention
        await Laang.edit(_["admin_14"].format(umention))

@Laang(["Ckick", "Cdkick"], devs=True)
@Laang(["kick", "dkick"], langs=True)
async def kick_user(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        Laang = await eor(message, _["p"])
        user_id, reason = await yins.extract_user_and_reason(message)
        if not user_id:
            return await Laang.edit(_["err_user"])
        if user_id == client.me.id:
            return await Laang.edit(_["admin_15"])
        if user_id in DEVS:
            return await Laang.edit(_["laang_2"])
        if user_id in (await yins.list_admins(client, message.chat.id)):
            return await Laang.edit(_["admin_16"])
        mention = (await client.get_users(user_id)).mention
        msg = _["admin_18"].format(mention, client.me.mention)
        if message.command[0][0] == "d":
            await message.reply_to_message.delete()
        if reason:
            msg += _["admin_4"].format(reason)
        try:
            await message.chat.ban_member(user_id)
            await Laang.edit(msg)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except ChatAdminRequired:
            await Laang.edit(_["admin_5"])
        except UserCreator:
            await Laang.edit(_["admin_6"])

@Laang(["Cpromote", "Cfullpromote"], devs=True)
@Laang(["promote", "fullpromote"], langs=True)
async def promote(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        user_id = await yins.extract_user(message)
        umention = (await client.get_users(user_id)).mention
        Laang = await eor(message, _["p"])
        if not user_id:
            return await Laang.edit(_["err_user"])
        if message.command[0][0] == "f":
            try:
                await message.chat.promote_member(
                    user_id,
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_change_info=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_promote_members=True,
                    ),
                )
                return await Laang.edit(_["admin_18"].format(umention))
            except ChatAdminRequired:
                return await Laang.edit(_["admin_5"])
            except UserCreator:
                return await Laang.edit(_["admin_6"])

        try:
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=False,
                ),
            )
            await Laang.edit(_["admin_19"].format(umention))
        except ChatAdminRequired:
            return await Laang.edit(_["admin_5"])
        except UserCreator:
            return await Laang.edit(_["admin_6"])

@Laang(["Cdemote"], devs=True)
@Laang(["demote"], langs=True)
async def demote(client: Client, message: Message, _):
    if await yins.CheckAdmin(client, message):
        user_id = await yins.extract_user(message)
        Laang = await eor(message, _["p"])
        if not user_id:
            return await Laang.edit(_["err_user"])
        if user_id == client.me.id:
            return await Laang.edit(_["admin_20"])
        try:
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                ),
            )
            umention = (await client.get_users(user_id)).mention
            await Laang.edit(_["admin_21"].format(umention))
        except (ChatAdminRequired, UserCreator):
            await Laang.edit(_["admin_5"])
        except UserCreator:
            await Laang.edit(_["admin_6"])

@Laang(["staff"])
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except AttributeError:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(f'[{nama}](tg://user?id={a.user.id})')
            else:
                admin.append(f'[{nama}](tg://user?id={a.user.id})')
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(f'[{nama}](tg://user?id={a.user.id})')
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = "**Admins in {}**\n".format(grup.title)
    teks += "╒═══「 Creator 」\n"
    for x in creator:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} Human Administrator 」\n".format(len(admin))
    for x in admin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} Bot Administrator 」\n".format(len(badmin))
    for x in badmin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╘══「 Total {} Admins 」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)

CMD_HELP.update(
    {"admins": (
        "admins",
        {
            "ban [reply/username/userid] [alasan]": "Membanned member dari grup.",
            "unban [reply/username/userid] [alasan]": "Membuka banned member dari grup.",
            "kick [reply/username/userid]": "Mengeluarkan pengguna dari grup.",
            "promote atau fullpromote": "Mempromosikan member sebagai admin atau cofounder.",
            "demote": "Menurunkan admin sebagai member.",
            "mute [reply/username/userid]": "Membisukan member dari Grup.",
            "unmute [reply/username/userid]": "Membuka mute member dari Grup.",
            "pin [reply]": "Untuk menyematkan pesan dalam grup.",
            "unpin [reply]": "Untuk melepaskan pin pesan dalam grup.",
            "setgpic [reply ke foto]": "Untuk mengubah foto profil grup",
        }
        )
    }
)
