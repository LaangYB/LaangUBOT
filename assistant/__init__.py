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

from config import *
from git import Repo
from pyLaang import PyrogramYB
from pyLaang.Clients import *
from pyLaang.config import Var


repo = Repo()
branch = repo.active_branch
yins = PyrogramYB()
var = Var()

logs = logging.getLogger(__name__)