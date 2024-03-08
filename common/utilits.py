

import aiohttp

API_URL = 'https://card.wb.ru/cards/v1/detail'


async def get_product_data(product_id):
    params = {
        'appType': 1,
        'curr': 'rub',
        'dest': -1257786,
        'spp': 30,
        'nm': product_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            return await response.json()


def format_product_data(product):
    name = product['name']
    id = product['id']
    price = product.get('salePriceU', product.get('priceU'))  # Используйте salePriceU, если он есть, иначе priceU
    rating = product['rating']
    quantity = sum(stock['qty'] for size in product['sizes'] for stock in size['stocks'])  # Суммируем количество по всем размерам и складам
    table = f"<b>Название</b>: {name}\n"
    table += f"<b>Артикул</b>: {id}\n"
    table += f"<b>Цена</b>: {price} ₽\n"
    table += f"<b>Рейтинг</b>: {rating}\n"
    table += f"<b>Количество на складах</b>: {quantity}"
    return table
