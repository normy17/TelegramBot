from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards.default as kb
from loader import dp


@dp.message_handler(text='Привет')
async def bot_hello(message: types.Message):
    await message.answer(f'Привет, {message.from_user.username}', reply_markup=kb.keybords.hello_kb)
