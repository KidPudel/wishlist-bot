# echo

import sys
import logging
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

TOKEN = os.environ.get("WISHLIST_BOT_TOKEN")

dp = Dispatcher()

@dp.message(Command("start", prefix="/"))
async def start_handler(message: Message):
    await message.answer(text=f"Hi, {message.from_user.first_name}!\nLet's make some wishes ✨\n\nTo see my functionality, you can look up the list of commands. 👇")


async def main():
    if TOKEN != None:
        bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
        await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())