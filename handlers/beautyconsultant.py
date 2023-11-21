from aiogram import Router, F, types
from aiogram.filters import Command


bc_router = Router()

"""создали обработчик который спрашивает тип кожи и отпрвляет уход за кожей по типу """
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
    reply_markup = kb)


@bc_router.message(F.text == "чувствительная кожа")
async def sensitiveskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-Beauty of Joseon\n"
        "умывашка- SKIN LAB с гиарулоновой капсулой\n"
        "тонер-ROUND LAB с морской солью\n"
        "крем-ELLO\n"
        "спф крем - PURITO\n"

    )

@bc_router.message(F.text == "сухая кожа")
async def dryskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-SIORIS\n"
        "умывашка-SUNJUNG\n"
        "тонер-ROUND LAB с березовым соком\n"
        "крем-TOCOBO\n"
        "спф крем- ROUND LAB с березовым соком\n"
    )

@bc_router.message(F.text == "жирная кожа")
async def oilskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-Dr.Althea\n"
        "умывашка-COSRX low pH\n"
        "тонер- ROUND LAB с бобовым экстактом\n"
        "крем-SKIN 1004 CENTELLA\n"
        "спф крем - ROUND LAB с березовым соком\n"
    )

@bc_router.message(F.text == "комбинированная кожа")
async def combiskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло-SKIN 1004 centella\n"
        "умывашка-round lab с березовым соком\n"
        "тонер- Dr. Althea\n"
        "крем-SKIN 1004 centella\n"
        "спф крем - ROUND LAB с березовым соком\n"
    )

@bc_router.message(F.text == "нормальная кожа")
async def normalskin_care(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(
        "гидрофильное масло- Dr.Ceuracle Pro-Balance\n"
        "умывашка- CeraVe с церамидом\n"
        "тонер-Beauty of Jesoun\n"
        "крем- Pyunkang Yul\n"
        "спф крем - Dr.Ceuracle Cica Regen Vegan Sun\n"
    )