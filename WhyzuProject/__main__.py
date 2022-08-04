# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/Whyzu-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/Whyzu-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import importlib

from WhyzuProject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from WhyzuProject.helpers.misc import heroku
from WhyzuProject.modules import ALL_MODULES

MSG_ON = """
🔥 **Whyzu-Userbot Berhasil Di Aktifkan**
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
            await bot.join_chat("WhyzuCH")
            await bot.join_chat("WhyzuNotSupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            LOGGER("WhyzuProject").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("WhyzuProject").info(f"Whyzu-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("WhyzuProject").info("Starting Whyzu-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
