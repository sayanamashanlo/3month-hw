import asyncio
import logging
from aiogram.types import BotCommand
from bot import dp, bot
from handlers import (
        start_router,
        picture_router,
        info_router,
        bc_router,
        questions_router
    )

"""ниже создали меню для бота set my commands"""
async def main():
    await bot.set_my_commands([
     BotCommand(command="start", description="начало"),
     BotCommand(command="myinfo", description="myinfo"),
     BotCommand(command="beauty", description="консультация"),
     BotCommand(command="quest", description="опросник")

    ])


    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(info_router)
    dp.include_router(bc_router)
    dp.include_router(questions_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())




