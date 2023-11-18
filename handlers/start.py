from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()


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