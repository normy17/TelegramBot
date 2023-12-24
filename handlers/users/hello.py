import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards.default as kb
from loader import dp, bot


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


@dp.message_handler(commands=['coaches'])
async def bot_hello(message: types.Message):
    await message.answer(text='Список тренеров:', reply_markup=kb.keybords.inline_kb)


@dp.callback_query_handler(lambda b: b.data.startswith('coach_'))
async def button_check(callback_query: types.CallbackQuery):
    coach_name = callback_query.data.split('_')[1]
    coach_info = f'*Информация о тренере {coach_name}*'
    await bot.send_message(callback_query.from_user.id, coach_info)


@dp.message_handler(commands=['groups'])
async def bot_hello(message: types.Message):
    await message.answer(text='Список групповых занятий:', reply_markup=kb.keybords.inline_kb2)


@dp.callback_query_handler(lambda b: b.data.startswith('class_'))
async def button_check(callback_query: types.CallbackQuery):
    class_name = callback_query.data.split('_')[1]
    class_info = f'*Информация о групповом занятии "{class_name}"*'
    await bot.send_message(callback_query.from_user.id, class_info)

days = ['Понедельник: 9:00 - Утренний йога-класс, 12:00 - Силовая тренировка "BodyPump", 18:00 - Кардио-тренировка "Spinning"',
        'Вторник: 10:00 - Зумба, 14:00 - Пилатес, 19:00 - Функциональная тренировка "CrossFit"',
        'Среда: 8:00 - Утренний беговой клуб, 13:00 - Тренировка на TRX, 17:00 - Йога для начинающих',
        'Четверг: 11:00 - Аэробика, 15:00 - Танцевальный фитнес, 20:00 - Стретчинг и релаксация',
        'Пятница: 9:30 - Тренировка "HIIT", 16:00 - Силовая тренировка "BodyPump", 16:00 - Силовая тренировка "BodyPump"',
        'Суббота: 10:00 - Зумба, 13:00 - Пилатес, 16:00 - Функциональная тренировка "CrossFit"',
        'Воскресенье: 11:00 - Аэробика, 15:00 - Танцевальный фитнес, 18:00 - Стретчинг и релаксация']


@dp.message_handler(commands=['week'])
async def start(message: types.Message):
    await message.answer("\n".join(days))


@dp.message_handler(commands=['today'])
async def start(message: types.Message):
    today = datetime.datetime.now().weekday()
    await message.answer(f'{days[today]}')