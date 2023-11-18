from aiogram import Router, types
from aiogram.filters import Command
import random
from aiogram import Bot

picture_router = Router()

@picture_router.message(Command('pic'))
async def send_picture(message: types.Message):
    file1 = types.FSInputFile("images/flag_turciya.jpg")
    file2 = types.FSInputFile("images/flag_argentina.jpg")
    file3 = types.FSInputFile("images/flag_britaniya.jpg")
    file4 = types.FSInputFile("images/flag_kirgiziya.jpg")
    file5 = types.FSInputFile("images/flag_saudovskaya_araviya.jpg")
    files_list = [file5, file4, file3, file1, file2]
    file = random.choice(files_list)
    await Bot.send_photo(chat_id=message.from_user.id,
                         photo=file)


def pic():
    return None