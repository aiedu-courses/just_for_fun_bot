from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

BOT_TOKEN = "..."

dp = Dispatcher()
bot = Bot(BOT_TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def echo_handler(message):
    await message.answer(message.text)

dp.run_polling(bot)
