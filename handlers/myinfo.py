
from aiogram import Router, types
from aiogram.filters import Command


info_router = Router()

@info_router.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш username: {username}")
