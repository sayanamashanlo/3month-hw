from aiogram import Router, F, types
from aiogram.filters import Command


bc_router = Router()


@bc_router.message(Command("beauty"))
async def beaty(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="чувствительная кожа")
            ],
            [
                types.KeyboardButton(text="сухая кожа")
            ],
            [
                types.KeyboardButton(text="жирная кожа")
            ],
            [
                types.KeyboardButton(text="комбинированная кожа")
            ],
            [
                types.KeyboardButton(text="нормальная кожа")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите свой тип кожи:",
    reply_markup=kb)


@bc_router.message(F.text == "чувствительная кожа")
async def sensitiveskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-"
        "умывашка-"
        "тонер-"
        "крем-"
        "спф крем"

    )

@bc_router.message(F.text == "сухая кожа")
async def dryskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-"
        "умывашка-"
        "тонер-"
        "крем-"
        "спф крем"
    )

@bc_router.message(F.text == "жирная кожа")
async def oilskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-"
        "умывашка-"
        "тонер-"
        "крем-"
        "спф крем"
    )

@bc_router.message(F.text == "комбинированная кожа")
async def combiskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-"
        "умывашка-"
        "тонер-"
        "крем-"
        "спф крем"
    )

@bc_router.message(F.text == "нормальная кожа")
async def normalskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-"
        "умывашка-"
        "тонер-"
        "крем-"
        "спф крем"
    )