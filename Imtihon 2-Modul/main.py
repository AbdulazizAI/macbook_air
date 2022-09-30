from telegram.ext import CommandHandler, Updater, CallbackContext
from telegram import Update
import logging
import constants


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom, men python botiman. Ko\'proq Ma\'lumot uchun / help buyrug\'ini bosing ko\'ring')



def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Buyruqlar ro'yxati:")
    update.message.reply_text('/add <1-Num> <2-Num>')
    update.message.reply_text('/subtract <1-Num> <2-Num>')
    update.message.reply_text('/multiply <1-Num> <2-Num>')
    update.message.reply_text("/divide <1-Num> <2-Num>")



def add(update: Update, context: CallbackContext):
    try:
        a = int(context.args[0])+int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Kechirasiz, men buni tushunmiyapman!')



def subtract(update: Update, context: CallbackContext):
    try:
        a = int(context.args[0])-int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Kechirasiz, men buni tushunmiyapman!')



def multiply(update: Update, context: CallbackContext):
    try:
        a = int(context.args[0])*int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Kechirasiz, men buni tushunmiyapman!')



def divide(update: Update, context: CallbackContext):
    try:
        a = int(context.args[0])/int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Kechirasiz, men buni tushunmiyapman!')




def main():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    updater = Updater(token=constants.key)
    dispatch = updater.dispatcher
    help_handler = CommandHandler('help', help_command)
    subtract_handler = CommandHandler('subtract', subtract)
    multiply_handler = CommandHandler('multiply', multiply)
    add_handler = CommandHandler('add', add)
    divide_handler = CommandHandler('divide', divide)
    start_handler = CommandHandler('start', start)
    dispatch.add_handler(help_handler)
    dispatch.add_handler(add_handler)
    dispatch.add_handler(subtract_handler)
    dispatch.add_handler(multiply_handler)
    dispatch.add_handler(divide_handler)
    dispatch.add_handler(start_handler)
    updater.start_polling(poll_interval=2)
    updater.idle()


main()
