from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Constants
TOKEN: Final[str] = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT_USERNAME: Final[str] = "python_invictus_bot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter Python programming... 🐍")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type something, and I'll respond.")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command.")


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Pleased to meet you; hope you guessed my name?"

    if "how are you" in processed:
        return "I am good, thanks."

    if "i love python" in processed:
        return "Python is cool!"

    return "I do not understand."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Log
    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    # Handle message type
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # Reply
    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


def main():
    print("Starting up bot....")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling -- check for messages in x amount of seconds
    print("Polling...")
    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()
