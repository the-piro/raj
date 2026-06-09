from bot import Bot
from pyrogram import idle
import os , shutil

async def restart():
    if os.path.exists('.restartmsg'):
        with open(".restartmsg") as f:
            chat_id, msg_id = map(int, f)
        try:
            await Bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="<b><i>Restarted !</i></b>")
            os.remove('.restartmsg')
        except Exception as e:
            LOGGER(__name__).error(f'Restarting ERROR - {e}')

try:
    Bot.loop.run_until_complete(restart())
    Bot.LOGGER(__name__).info('Bot Started !')
    Bot.loop.run_forever()
    idle()
except Exception as e:
    [shutil.rmtree(i) for i in ('downloads')]
    Bot.LOGGER(__name__).error(e)
    Bot.LOGGER(__name__).info('Bot Stopped !')
    Bot.stop()