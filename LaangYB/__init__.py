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

import logging

from typing import Optional

from fipper import Client
from fipper.raw.functions.channels import GetFullChannel
from fipper.raw.functions.messages import GetFullChat
from fipper.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from fipper.types import Message

from config import *
from git import Repo
from pyLaangYB import PyrogramYB
from pyLaang.Clients import *
from pyLaang.config import Var
from pyLaang.pyrogram import eod, eor


flood = {}
OLD_MSG = {}
repo = Repo()
branch = repo.active_branch
yins = PyrogramYB()
var = Var()
hndlr = [
    f"{var.HNDLR[0]}",
    f"{var.HNDLR[1]}",
    f"{var.HNDLR[2]}",
    f"{var.HNDLR[3]}",
]
logs = logging.getLogger(__name__)

file = './cache/'
cache = "cache/{}.png"
cache_thumb = "cache/thumb{}.png"
font = "assets/font.ttf"
font2 = "assets/font2.ttf"