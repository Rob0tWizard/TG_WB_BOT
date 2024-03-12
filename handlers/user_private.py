from aiogram import types,  F, Router

from aiogram.filters import Command, CommandStart, or_f
from aiogram.filters.state import StatesGroup, State, StateFilter
from aiogram.fsm.context import FSMContext


from common.utilits import format_product_data, get_product_data
from keyboards import reply
from keyboards.reply import start_kb

user_private_router = Router()


class ProductInfo(StatesGroup):
    waiting_for_id = State()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    keyboard = start_kb
    await message.answer("Выберите одну из команд:", reply_markup=keyboard)


@user_private_router.message(StateFilter(None), or_f(Command('vendor'), F.text.lower() == "получить информацию по товару"))
async def get_product_info(message: types.Message, state: FSMContext):
    await state.set_state(ProductInfo.waiting_for_id)
    await message.answer("Пожалуйста, введите артикул товара.")


@user_private_router.message(ProductInfo.waiting_for_id)
async def process_product_id(message: types.Message, state: FSMContext):
    product_id = message.text
    data = await get_product_data(product_id)
    print(data)
    if 'data' in data and 'products' in data['data']:
        product = data['data']['products'][0]
        text = format_product_data(product)
        await message.answer(text, parse_mode='HTML')
    else:
        await message.answer("Не удалось получить информацию о товаре.")
    await state.clear()


@user_private_router.message(or_f(Command('stop'), (F.text == 'Остановить уведомления')))
async def stop_cmd(message: types.Message):
    await message.answer("stop",
                         reply_markup=reply.del_kb)


@user_private_router.message(F.text == 'Получить информацию из БД')
@user_private_router.message(Command('info'))
async def info_cmd(message: types.Message):
    await message.answer("DB",
                         reply_markup=reply.del_kb)

# @user_private_router.message(F.text)
# async def echo(message: types.Message):
#    await message.answer(message.text)
