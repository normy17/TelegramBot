import datetime

from aiogram import types

import keyboards.default as kb
from loader import dp, bot, omdb_api_key

from requests import request


def create_response_message(response):
    message = f'{response["Title"]}\n' \
              f'Год выпуска: {response["Year"]}\n' \
              f'Рейтинг: {response["imdbRating"]}\n' \
              f'Длительность: {response["Runtime"]}\n' \
              f'Режиссер: {response["Director"]}\n' \
              f'Актеры: {response["Actors"]}'
    return message


@dp.message_handler(commands=['film'])
async def bot_film(message: types.Message):
    params = message.text.split()
    request_URL = ''
    if len(params) == 1:
        await message.answer('Недостаточно параметров. Примеры использования параметров:\n'
                             '1. <b>/film</b> название-фильма\n'
                             '2. /film название-фильма год_фильма\n'
                             '3. /film imdb_код_фильма_imdb>\n')
        return
    elif len(params) == 2:
        if params[1][:5] == 'imdb_':
            request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&i={params[1][5:]}'
        else:
            request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&t={params[1]}'
    else:
        request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&t={params[1]}&y={params[2]}'
    response = request('GET', request_URL).json()
    if response['Response'] == "True":
        await message.answer(create_response_message(response))
    else:
        await message.answer(response['Error'])


@dp.message_handler(commands=['random'])
async def bot_random(message: types.Message):
    numbers = message.text.split()
    if len(numbers) != 3:
        await message.answer('Неправильное количество параметров.')
        return
    json_params = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {"apiKey": "016e4ceb-a08d-497c-9c58-451028b0e5f0",
                   "n": 1,
                   "min": numbers[1],
                   "max": numbers[2]},
        "id": 1
    }
    response = request(method='GET', url='https://api.random.org/json-rpc/4/invoke', json=json_params).json()
    if response['result']:
        await message.answer(response['result']['random']['data'][0])
    else:
        await message.answer(response['Error'])


@dp.message_handler(text='Привет')
async def bot_hello(message: types.Message):
    await message.answer(f'Привет, {message.from_user.username}')


@dp.message_handler(text='Писатель')
async def bot_hello(message: types.Message):
    await message.answer('Хемингуэй')


@dp.message_handler(text='Поэт')
async def bot_hello(message: types.Message):
    await message.answer('Шекспир')


@dp.message_handler(text='Книга')
async def bot_hello(message: types.Message):
    await message.answer('Три товарища')


@dp.message_handler(text='Монолог')
async def bot_hello(message: types.Message):
    await message.answer('Быть или не быть')

# @dp.message_handler(commands=['coaches'])
# async def bot_hello(message: types.Message):
#     await message.answer(text='Список тренеров:', reply_markup=kb.keybords.inline_kb)
#
#
# @dp.callback_query_handler(lambda b: b.data.startswith('coach_'))
# async def button_check(callback_query: types.CallbackQuery):
#     coach_name = callback_query.data.split('_')[1]
#     coach_info = f'*Информация о тренере {coach_name}*'
#     await bot.send_message(callback_query.from_user.id, coach_info)
#
#
# @dp.message_handler(commands=['groups'])
# async def bot_hello(message: types.Message):
#     await message.answer(text='Список групповых занятий:', reply_markup=kb.keybords.inline_kb2)
#
#
# @dp.callback_query_handler(lambda b: b.data.startswith('class_'))
# async def button_check(callback_query: types.CallbackQuery):
#     class_name = callback_query.data.split('_')[1]
#     class_info = f'*Информация о групповом занятии "{class_name}"*'
#     await bot.send_message(callback_query.from_user.id, class_info)
#
#
# days = [
#     'Понедельник: 9:00 - Утренний йога-класс, 12:00 - Силовая тренировка "BodyPump", 18:00 - Кардио-тренировка "Spinning"',
#     'Вторник: 10:00 - Зумба, 14:00 - Пилатес, 19:00 - Функциональная тренировка "CrossFit"',
#     'Среда: 8:00 - Утренний беговой клуб, 13:00 - Тренировка на TRX, 17:00 - Йога для начинающих',
#     'Четверг: 11:00 - Аэробика, 15:00 - Танцевальный фитнес, 20:00 - Стретчинг и релаксация',
#     'Пятница: 9:30 - Тренировка "HIIT", 16:00 - Силовая тренировка "BodyPump", 16:00 - Силовая тренировка "BodyPump"',
#     'Суббота: 10:00 - Зумба, 13:00 - Пилатес, 16:00 - Функциональная тренировка "CrossFit"',
#     'Воскресенье: 11:00 - Аэробика, 15:00 - Танцевальный фитнес, 18:00 - Стретчинг и релаксация']
#
#
# @dp.message_handler(commands=['week'])
# async def start(message: types.Message):
#     await message.answer("\n".join(days))
#
#
# @dp.message_handler(commands=['today'])
# async def start(message: types.Message):
#     today = datetime.datetime.now().weekday()
#     await message.answer(f'{days[today]}')
