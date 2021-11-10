import Constants as keys
# import telegram.ext 
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import Responses as R

print("Bot started...")

def start_command(update,context):
    update.message.reply_text('Type something random to get started!')

def help_command(update,context):
    update.message.reply_text('If any problem arrives contact @prasanthNalluri!')

def handle_message(update,context):
    text = str(update.message.text).lower()
    response =R.sample_responses(text)

    update.message.reply_text(response)

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True) 
    dp = Updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(CommandHandler("start", help_command))

dp.add_handler(MessageHandler(Filters.txt, handle_message))

dp.add_error_handler(error)

Updater.start_polling()
Updater.idle()

main()