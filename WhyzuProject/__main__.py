# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/nathxe/PyroNath-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/nathxe/PyroNath-Userbot/blob/main/LICENSE/>.
#
# t.me/nathsupport & t.me/nathaellxx

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from WhyzuProject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from WhyzuProject.helpers.misc import heroku
from WhyzuProject.modules import ALL_MODULES

MSG_ON = """
⚡ **PyroNath-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"WhyzuProject.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("nathaellxx")
            await bot.join_chat("nathsupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            LOGGER("WhyzuProject").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("WhyzuProject").info(f"PyroNath-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("WhyzuProject").info("Starting PyroNath-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
