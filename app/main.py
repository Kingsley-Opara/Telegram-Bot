from config import get_config 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from helpers import get_result
from fastapi import FastAPI

fastapi_app = FastAPI()


@fastapi_app.get('/')
def home():
    return{"hello": "world"}

config = get_config()

BOT_USERNAME = config.BOT_USERNAME

TOKEN = config.TOKEN

async def start_command(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I was trained to answer pharmacology questions only!")

async def help_command(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I was trained to answer pharmacology questions. Please, do drop your question")

async def custom_command(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


def handle_response(text:str):
    return get_result(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == "group":
        if BOT_USERNAME in text:
            text = text.replace(BOT_USERNAME, " ").strip()
            response = handle_response(text)

        else:
            return
    response =  handle_response(text)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")



if __name__ == "__main__":
    print("start")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print("polling......")
    app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url="https://telegram-chat-bot.back4app.io/home"
    )
