import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
