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