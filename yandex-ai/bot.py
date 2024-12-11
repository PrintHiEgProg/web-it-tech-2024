from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Токен вашего Telegram бота
TELEGRAM_BOT_TOKEN = "7970877206:AAGKEo257rO7-oj3tLMck50hixrJ8XPTgow"

# Путь к файлу, где будут храниться ID пользователей
USERS_FILE = "joined.txt"

# Функция для проверки наличия ID пользователя в файле
def is_user_exists(user_id: str) -> bool:
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as file:
        return user_id in file.read().splitlines()

# Функция для записи ID пользователя в файл, если его там нет
def add_user(user_id: str):
    if not is_user_exists(user_id):
        with open(USERS_FILE, "a") as file:
            file.write(f"{user_id}\n")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    if not is_user_exists(user_id):
        add_user(user_id)  # Добавляем ID пользователя в файл, если его там нет
        await update.message.reply_text("Добро пожаловать! Ваш ID записан.")
    else:
        await update.message.reply_text("Вы уже записаны в список.")

# Основная функция для запуска бота
def main():
    # Инициализация Application с токеном вашего бота
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()