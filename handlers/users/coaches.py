import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command
from data.fitness_club_info import coaches, groups
from keyboards.inline.coach_kb import coach_kb, group_kb

from loader import dp, bot


@dp.message_handler(Command('coaches'))
async def bot_coaches(message: types.Message):
    await message.answer('Наши тренера:', reply_markup=coach_kb)


@dp.callback_query_handler(lambda b: b.data in ['coach-0', 'coach-1'])
async def button_check(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, coaches[int(callback_query.data.split('-')[1])].desc)


@dp.message_handler(Command('groups'))
async def bot_groups(message: types.Message):
    await message.answer('Наши группы:', reply_markup=group_kb)


@dp.callback_query_handler(lambda b: b.data in ['group-0', 'group-1', 'group-2'])
async def button_check(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    group = groups[int(callback_query.data.split('-')[1])]
    await bot.send_message(callback_query.from_user.id, f'{group.name}\n'
                                                        f'{group.desc}\n')


@dp.message_handler(Command('today'))
async def bot_today(message: types.Message):
    today = datetime.datetime.now().weekday()
    times = {}
    for group in groups:
        if group.time[today] != "":
            times[group.time[today]] = group.name

    shedule = ''
    for key in sorted(list(times.keys())):
        shedule += f'{key} - {times[key]} \n'
    await message.answer(shedule)

