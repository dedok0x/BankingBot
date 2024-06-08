import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TOKEN


async def echo(message: Message):
    await message.answer(message.text)

async def start():
    bot = Bot(TOKEN)

    dp = Dispatcher()

    dp.message.register(echo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())