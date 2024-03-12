import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from database.engine import drop_db, create_db
from common.bot_cmd_list import private
from handlers.user_private import user_private_router

ALLOW_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher()
dp.include_router(user_private_router)


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    #dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)


asyncio.run(main())
