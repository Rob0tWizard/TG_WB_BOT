from aiogram import types, Router

from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("старт")


@user_private_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)
