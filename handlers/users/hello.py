from aiogram import types

from loader import dp, omdb_api_key

from requests import request
from json import dumps


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
    if len(numbers) != 4:
        await message.answer(
            'Неправильное количество параметров. Нужно ввести начало диапазона, конец и количество чисел. Пример: "/random 1 10 4"')
        return
    json_params = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {"apiKey": "016e4ceb-a08d-497c-9c58-451028b0e5f0",
                   "n": numbers[3],
                   "min": numbers[1],
                   "max": numbers[2]},
        "id": 1
    }
    encoded_data = dumps(json_params)
    response = request(method='GET', url='https://api.random.org/json-rpc/1/invoke', data=encoded_data).json()
    if response['result']:
        await message.answer(response['result']['random']['data'])
    else:
        await message.answer(response['Error'])


@dp.message_handler(commands=['random2'])
async def bot_random(message: types.Message):
    words = message.text.split()
    if len(words) != 2 or (words[1] != 'Орел' or words[1] != 'Решка'):
        await message.answer('Неправильный ввод. Нужно выбрать "Орел" или "Решка". Пример: "/random2 Решка"')
        return
    json_params = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {"apiKey": "016e4ceb-a08d-497c-9c58-451028b0e5f0",
                   "n": 1,
                   "min": 1,
                   "max": 2},
        "id": 1
    }
    encoded_data = dumps(json_params)
    response = request(method='GET', url='https://api.random.org/json-rpc/1/invoke', data=encoded_data).json()
    if response['result']:
        if response['result']['random']['data'][0] == 1 and words[1] == "Орел":
            await message.answer("Орел\nВы выиграли")
        elif response['result']['random']['data'][0] == 1 and words[1] == "Решка":
            await message.answer("Орел\nВы проиграли")
        elif response['result']['random']['data'][0] == 2 and words[1] == "Орел":
            await message.answer("Решка\nВы проиграли")
        elif response['result']['random']['data'][0] == 2 and words[1] == "Решка":
            await message.answer("Решка\nВы выиграли")
    else:
        await message.answer(response['Error'])