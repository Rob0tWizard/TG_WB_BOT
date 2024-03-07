import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_private_router

load_dotenv(find_dotenv())

ALLOW_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)


asyncio.run(main())