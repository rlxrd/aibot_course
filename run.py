import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN

from app.admin import admin
from app.user import user

from app.database.models import async_main


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(user, admin)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


async def on_startup(dispatcher):
    await async_main()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
