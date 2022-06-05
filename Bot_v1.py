from telegram import Update
from telegram import Bot
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater              #Подключаю библеотек
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request


button_help = 'Помощь'

def button_help_handler(update: Update, context: CallbackContext):  #Функция отвечающая на нажатие кнопки
    update.message.reply_text(
        text='Это Помощь',
        reply_markup=ReplyKeyboardRemove(),
    )

def message_handler(update: Update, context: CallbackContext):   #Функция отвечающая на сообщения
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(button_help),                                 #Добавляю кнопку
            ],
        ],
        resize_keyboard=True,                                    #Если понадобится изменить размер , то он подсьроится
    )
    update.message.reply_text(
        text='Жми кнопку!',
        reply_markup=reply_markup
    )

def main():
    print('Start')
    red = Request(
        connect_timeout=0.5,
    )
    bot = Bot(                                                   #Конструкция , которя делает запрос
        request=red,
        token='5479031251:AAEKmIniuGcV4fT0w2MNBD83QN2vdp41VHg',  # Ввожу токен созданого бота(из ботфазера)
    )
    updater = Updater(                                           #Конструкция , которая ходит в тг за обновлениями
        bot=bot,
        use_context=True,
    )
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()          #Обновления
    updater.idle()             #Остановка обновлений после одного раза
    print('Finish')

if __name__ == '__main__':
    main()

