import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.start import register_start_handlers
from handlers.quiz import register_quiz_handlers
from database import create_table

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7267050904:AAF6K6i4xcODQZqyvZXC0bU1gWjMz7Pd_Kk'

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher(storage=MemoryStorage())

async def main():
    # Создаем таблицу базы данных
    await create_table()

    # Регистрируем хэндлеры
    register_start_handlers(dp)
    register_quiz_handlers(dp)

    # Запуск процесса поллинга новых апдейтов
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
