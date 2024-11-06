from config import get_config 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


config = get_config()

BOT_USERNAME = config.BOT_USERNAME



