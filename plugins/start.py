from bot import Bot
from pyrogram import filters
from config import ADMINS
import os , sys , shutil

@Bot.on_message(filters.command("start") & filters.private & filters.user(ADMINS))
async def start_cmd(bot, message):
    await message.reply_text("<b>Hello! I am Zake.</b>" , True)

@Bot.on_message(filters.command(['restart']) & filters.private & filters.user(ADMINS))
async def restart(app , message):
    [shutil.rmtree(i) for i in ('downloads',)]
    msg = await message.reply_text('<b><i>Restarting...</i></b>' , True)
    with open(".restartmsg", "w") as f:
        f.write(f"{msg.chat.id}\n{msg.id}\n")
    os.execl(sys.executable, sys.executable, '-B' , "main.py")
