import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards.default as kb
from loader import dp, bot


@dp.message_handler(text='Привет')
async def bot_hello(message: types.Message):
    await message.answer(f'Привет, {message.from_user.username}', reply_markup=kb.keybords.inline_kb)


@dp.callback_query_handler(lambda b: b.data == 'hello_btn')
async def button_check(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг']
    today = datetime.datetime.now().weekday()

    await bot.send_message(callback_query.from_user.id, f'{days[today]}')