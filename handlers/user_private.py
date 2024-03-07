from aiogram import F, types, Router

from aiogram.filters import CommandStart, Command

from keyboards import reply

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("привет", reply_markup=reply.start_kb)


@user_private_router.message(Command('1'))
async def menu_cmd(message: types.Message):
    await message.answer("menu 1")


@user_private_router.message(Command('2'))
async def menu_cmd(message: types.Message):
    await message.answer("menu 2")


@user_private_router.message(Command('3'))
async def menu_cmd(message: types.Message):
    await message.answer("menu 3")


@user_private_router.message(F.text)
async def echo(message: types.Message):
    await message.answer(message.text)




