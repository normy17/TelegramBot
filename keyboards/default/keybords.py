from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

couches = ['тренер 1', 'тренер 2']
inline_kb = InlineKeyboardMarkup()
for couch in couches:
    button = InlineKeyboardButton(couch, callback_data='hello_btn')
    inline_kb.add(button)


