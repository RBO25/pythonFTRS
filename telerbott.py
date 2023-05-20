

import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import datetime
from aiogram.utils import executor
from config import bot_token


b = Bot(token=bot_token)
dp = Dispatcher(b)

@dp.message_handler(commands=['start', 'help'])
async def help(message: types.Message):
    text = 'Чтобы начать работу введите команду боту количество символов пароля'
    await message.reply(text)


@dp.message_handler()
async def passgen(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("👋 Once more")
    markup.add(button)

    try:
        password = ''

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '1234567890'
        signs = '!@#$%^&'
        sumlist = alphabet + alphabet2 + digits +signs
        for i in range(1, 25):
            password += random.choice(sumlist)
        await message.reply(password, reply_markup=markup)

    except:
        await message.reply('Error')


if __name__ == '__main__':
    executor.start_polling(dp)