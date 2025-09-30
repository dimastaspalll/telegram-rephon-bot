import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters

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

async def show_manuals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(text=name, url=url)] for name, url in manuals.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        "Выберите мануал, который вам нужен:",
        reply_markup=reply_markup
    )

async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Начать", callback_data="start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Привет! Это бот с мануалами для менеджеров Rephon.\nНажмите кнопку ниже, чтобы начать:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()

    # Обработчик любого текста до нажатия кнопки
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, welcome_message))
    # Обработчик нажатия кнопки "Начать"
    app.add_handler(CallbackQueryHandler(show_manuals, pattern="start"))

    print("Бот запущен...")
    app.run_polling()
