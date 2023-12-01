from aiogram import Router, F,  types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from db.queries import save_questionaire

questions_router = Router()

# FSM - FINITE STATE MACHINE(конечный автомат)
"""опросник для бота"""

"""FSM диалог с пользователем"""

"""в классе создали шаги"""

class Questionare(StatesGroup):
    name = State()
    age = State()
    country = State()
    favoritebook = State()
    favotitefilm = State()
    favoriteserial =State()


@questions_router.message(Command("stop"))
@questions_router.message(F.text == "stop")
async def stop_questions(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вопросы прерваны")

@questions_router.message(Command("quest"))
async def start_questions(message: types.Message, state:
FSMContext):
    await state.set_state(Questionare.name)
    await message.answer("Для выхода введите 'stop'")
    await message.answer("Как вас зовут?")


@questions_router.message(F.text, Questionare.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Questionare.age)
    await message.answer("Сколько вам лет?")



@questions_router.message(F.text, Questionare.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(age) < 12 or int(age) > 100:
        await message.answer("Возраст должен быть от 12 до 100")
    else:
        await state.update_data(age=int(age))

    await state.set_state(Questionare.country)
    await message.answer("Из какой вы страны?")


@questions_router.message(F.text, Questionare.country)
async def process_coutry(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await state.set_state(Questionare.favoritebook)
    await message.answer("Какая ваша любимая книга?/название")


@questions_router.message(F.text, Questionare.favoritebook)
async def favorite_book(message: types.Message, state: FSMContext):
    await state.update_data(favoritebook=message.text)
    await state.set_state(Questionare.favotitefilm)
    await message.answer("Какой ваш любимый фильм?")


@questions_router.message(F.text, Questionare.favotitefilm)
async def favorite_film(message: types.Message, state: FSMContext):
    await state.update_data(favotitefilm=message.text)
    await state.set_state(Questionare.favoriteserial)
    await message.answer("Какой ваш самый любимый сериал?/название")


@questions_router.message(F.text, Questionare.favoriteserial)
async def favorite_serial(message: types.Message, state: FSMContext):
    await state.update_data(favoriteserials=message.text)
    data = await state.get_data()
    save_questionaire(data)
    # print(data)
    await state.clear()
    await message.answer("СПАСИБО ЗА ОТВЕТЫ, МЫ СВЯЖЕМСЯ С ВАМИ!")
