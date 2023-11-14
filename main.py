import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!")


@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш username: {username}")


@dp.message(Command('pic'))
async def send_picture(message: types.Message):
    file1 = types.FSInputFile("images/flag_turciya.jpg")
    file2 = types.FSInputFile("images/flag_argentina.jpg")
    file3 = types.FSInputFile("images/flag_britaniya.jpg")
    file4 = types.FSInputFile("images/flag_kirgiziya.jpg")
    file5 = types.FSInputFile("images/flag_saudovskaya_araviya.jpg")
    files_list = [file5, file4, file3, file1, file2]
    file = random.choice(files_list)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=file)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
