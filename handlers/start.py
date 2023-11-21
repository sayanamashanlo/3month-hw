from aiogram import Router, F, types
from aiogram.filters import Command
from db import queries

start_router = Router()

@start_router.message(Command('show_answer'))
async def show_answer(message: types.Message):
    answers = queries.get_answer()
    answers_str = '\n'.join(map(str, answers))
    await message.answer(answers_str)
@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш сайт", url="https://hellobeauty.kg/"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about"
                )
            ],
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}!",
                        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("BEAUTY SHOP")