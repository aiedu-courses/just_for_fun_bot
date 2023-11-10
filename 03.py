import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from config import BotSettings

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def echo_handler(message):
    await message.answer(message.text)


async def main():
    bot_settings = BotSettings()


    # настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: "
               "%(filename)s: "
               "%(levelname)s: "
               "%(funcName)s(): "
               "%(lineno)d:\t"
               "%(message)s",
    )

    # создаем бота
    bot = Bot(bot_settings.bot_token)
    logging.info("Бот запущен и готов к работе!")

    # опрашиваем телеграм в бесконечном цикле
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
