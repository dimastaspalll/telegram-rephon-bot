import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = os.getenv("API_TOKEN")

manuals = {
    "Курьер МСК": "https://teletype.in/@natasha_leo/tqHZ8o8QrUl",
    "Авито": "https://teletype.in/@natasha_leo/xrw0Y_rbnQg",
    "Подзаказы": "https://teletype.in/@natasha_leo/ZzY_u75V2rP",
    "Работа с заказами": "https://teletype.in/@natasha_leo/KOKvOdw7ghM",
    "Распорядок дня менеджера": "https://teletype.in/@natasha_leo/mkyZxhzpVa9",
    "Обмен товара": "https://teletype.in/@natasha_leo/SQ4fwWDfLb-",
    "Обработка заказа в базе 1С": "https://teletype.in/@natasha_leo/rnsd0T5dI0D",
    "Гарантия": "https://teletype.in/@natasha_leo/2jtoZJQfXH8",
    "Возврат денежных средств": "https://teletype.in/@natasha_leo/UV0LX0nCJpz"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Приветственная картинка (замени ссылку при желании)
    await update.message.reply_photo(
        photo="https://telegra.ph/file/пример_ссылки_на_картинку.jpg",
        caption="👋 Привет! Это бот с мануалами для менеджеров Rephon."
    )
    # Кнопки с мануалами
    keyboard = [[InlineKeyboardButton(text=name, url=url)] for name, url in manuals.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите мануал, который вам нужен:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
