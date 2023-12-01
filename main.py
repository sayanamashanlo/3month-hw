import asyncio
import logging
from aiogram.types import BotCommand
from bot import dp, bot, scheduler
from handlers import (
        start_router,
        picture_router,
        info_router,
        bc_router,
        questions_router,
        subscribe_router
    )
from db.queries import (init_db, create_tables, populate_tables)

from handlers.delayed_answer import set_mailing



async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()

    scheduler.add_job(set_mailing, 'interval', seconds=10, id='send_mailing', args=(dp,))
    scheduler.start()



"""ниже создали меню для бота set my commands"""
async def main():
    await bot.set_my_commands([
     BotCommand(command="start", description="начало"),
     BotCommand(command="myinfo", description="информация о себе"),
     BotCommand(command="picture", description="картинки"),
     BotCommand(command="shop", description="магазин косметики"),
     BotCommand(command="quest", description="вопросы"),
     BotCommand(command="check", description="проверка из db"),
     BotCommand(command="subscribe", description="Subscribe for our mailing")
    ])


    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(info_router)
    dp.include_router(bc_router)
    dp.include_router(questions_router)
    dp.include_router(subscribe_router)
    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())




