from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.fitness_club_info import coaches, groups

coach_kb = InlineKeyboardMarkup(row_width=1)
for i in range(len(coaches)):
    button = InlineKeyboardButton(coaches[i].name, callback_data=f'coach-{i}')
    coach_kb.add(button)

group_kb = InlineKeyboardMarkup(row_width=1)
for i in range(len(groups)):
    button = InlineKeyboardButton(groups[i].name, callback_data=f'group-{i}')
    group_kb.add(button)
