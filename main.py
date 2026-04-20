import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router

bot = Bot(token="8652461839:AAF1Guk51AHV_n2bPpkoPzWBOm3Q-B6mpko")
dp = Dispatcher()

async def main():
    dp.include_router(router)
    print("Бот запущен 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())