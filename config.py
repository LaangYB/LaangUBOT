from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


flood = {}
OLD_MSG = {}
MSG_PERMIT = (
    """
╔═════════════════════╗
│  𖣘 𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝙳𝙰𝚃𝙰𝙽𝙶 𝚃𝙾𝙳 𖣘ㅤ  ㅤ
╚═════════════════════╝
 ⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳
 ⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼
 ⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄
╔═════════════════════╗
│ㅤㅤ𖣘 𝙿𝙴𝚂𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𖣘ㅤㅤ
│ㅤㅤ   𖣘 Laang - 𝚄𝙱𝙾𝚃 𖣘ㅤㅤ
╚═════════════════════╝
"""
)


class Var:
    API_HASH = getenv("API_HASH")
    API_ID = int(getenv("API_ID", ""))
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/43d490b38cc1199e1706d.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Gw LaangUBOT Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    MONGO_URI = getenv("MONGO_URI", None)
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    PMPERMIT = bool(getenv("PMPERMIT", True))
    PERMIT_MSG = str(getenv("PERMIT_MSG", MSG_PERMIT))
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 5))
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
