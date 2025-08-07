import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import requests

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, который выдает случайные числа и интересные факты о них.")


# Генерация случайного числа и получение фактического описания
def generate_random_number_and_fact():
    number = random.randint(1, 200)
    response = requests.get(f'http://numbersapi.com/{number}')
    return f"Ваше число: {number}\nИнтересный факт: {response.text}"


# Обработчик команды /random
async def random_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = generate_random_number_and_fact()
    await update.message.reply_text(result)


if __name__ == '__main__':
    # Токен вашего Telegram-бота
    application = ApplicationBuilder().token('8107339762:AAF-43aB3BNT41dpVZm4RN_oaJfDO5wsSxk').build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random", random_command))

    # Запуск бота
    logger.info("Запускаю бота...")
    application.run_polling()