from aiogram import Router, F, types
from aiogram.filters import Command
from db.queries import get_products
from db.queries import get_product_by_category_id

bc_router = Router()

"""создали обработчик для магазина """
@bc_router.message(Command("shop"))
async def beauty(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="крем")
            ],
            [
                types.KeyboardButton(text="тонер")
            ],
            [
                types.KeyboardButton(text="сыворотка")
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите категорию уходового продукта:",
    reply_markup = kb)


@bc_router.message(F.text == "крем")
async def show_creams(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    creams = get_product_by_category_id(1)
    await message.answer(f"крема")
    for cream in creams:
        await message.answer(f"{cream[1]}\nPrice: {cream[2]}", reply_markup=kb)


@bc_router.message(F.text == "тонер")
async def show_toners(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    toners = get_product_by_category_id(2)
    await message.answer("тонеры", reply_markup=kb)
    for toner in toners:
        await message.answer(f"{toner[1]}\nPrice: {toner[2]}", reply_markup=kb)

@bc_router.message(F.text == "сыворотка")
async def show_serums(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    serums = get_product_by_category_id(3)
    await message.answer("сыворотки", reply_markup=kb)
    for serum in serums:
        await message.answer(f"{serum[1]}\nPrice: {serum[2]}", reply_markup=kb)