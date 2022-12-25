# Задача Семинар 9. Прикрутить бота к задаче о телефонном справочнике.
# Бот должен показать весь телефонный справочник, найти по фамилии, а 
# также предоставить возможность добавлять и удалять записи в справочнике.
# Проект выложить на гитхаб, добавить файл requirements.txt, в котором 
# указать необходимые библитеки для установки.
# Папку venv загружать на гитхаб не нужно!
# Команды телеграм-бота для телефонного справочника контактов:
# /shoall - показать все контакты; /show - показать один выбранный контакт
# /redact - редактировать выбранную запись; /add - добавить один контакт
# /delete - удалить выбранную запись; /find - найти контакт
# /start - старт бот; /stop - стоп бот
# =============================================================================
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from token_1 import token
from modeldb import *


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

TOKEN = token
db_f = 'phonescatalog.db'


def start(update, context):
    update.message.reply_text(
        "Привет. Я бот - телефонный справочник.\n"
        "Выбирите команду телефонного справочника:\n\n"
        "/showall - показать все контакты\n"
        "/show - показать один выбранный контакт\n"
        "/redact - редактировать выбранную запись\n"
        "/delete - удалить выбранную запись\n"
        "/add - добавить один контакт\n"
        "/find - найти контакт\n"
        "/start - старт бот; /stop - стоп бот\n")
        

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

def showall(update, context):
    update.message.reply_text('Выбрана команда - показать все контакты.\n'
            'Подтвердите команду - введите любую букву или цифру и ввод:\n')
    return 1

# def showallFunc(update, context):
#     value = db_view(db_f)
#     update.message.reply_text(f'Ответ = \n{value}')
#     return ConversationHandler.END

def showallFunc(update, context):
    value = db_view(db_f)
    update.message.reply_text('Ответ = \n')
    for s in value:
        update.message.reply_text(f'{s} \n')
    return ConversationHandler.END

def find(update, context):
    update.message.reply_text('Выбрана команда - найти контакт.\n'
                              'Введите фамилию или имя:\n')
    return 1

def findFunc(update, context):
    value = update.message.text
    res = db_one(value, db_f)
    update.message.reply_text(f'Ответ: {res}')
    return ConversationHandler.END

def show(update, context):
    update.message.reply_text('Выбрана команда - найти контакт по номеру.\n'
                              'Введите номер записи:\n')
    return 1

def showFunc(update, context):
    value = update.message.text
    res = db_num(value, db_f)
    update.message.reply_text(f'Ответ: {res}')
    return ConversationHandler.END

def add(update, context):
    update.message.reply_text('Выбрана команда - добавить один контакт.\n'
            'Введите через пробел - Фамилия Имя НомерТелефона должность:\n')
    return 1

def addFunc(update, context):
    value = update.message.text
    db_add(value, db_f)
    update.message.reply_text(f'Контакт добавлен: {value}')
    return ConversationHandler.END

def delete(update, context):
    update.message.reply_text('Выбрана команда - удалить один контакт.\n'
                              'Введите номер контакта для удаления:\n')
    return 1

def deleteFunc(update, context):
    value = update.message.text
    res = db_delete(value, db_f)
    update.message.reply_text(f'Контакт номер: {value} - {res}.')
    return ConversationHandler.END

def redact(update, context):
    update.message.reply_text('Выбрана команда - редактировать контакт.\n'
                              'Введите НомерКонтакта:\n')
    return 1

num = 0
def redact_date(update, context):
    global num
    num = update.message.text
    res = db_num(num, db_f)
    update.message.reply_text(f'Ответ: {res}')
    if res == 'Контакт не найден!':
        return ConversationHandler.END
    update.message.reply_text('Введите через пробел - \n'
                'Фамилия Имя НомерТелефона должность\n')
    return 2

def redactFunc(update, context):
    value = update.message.text
    v = value.split()
    db_redact(v, num, db_f)
    update.message.reply_text(f'Контакт номер {num} обновлён.')
    return ConversationHandler.END

def get_handler(command, func1, func2):
    hand = ConversationHandler(
            entry_points=[CommandHandler(command, func1)],
            states={1: [MessageHandler(Filters.text & ~Filters.command, func2)],
            },
            fallbacks=[CommandHandler('stop', stop)]
        )
    return hand


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    showall_handler = get_handler('showall', showall, showallFunc)
    find_handler = get_handler('find', find, findFunc)
    show_handler = get_handler('show', show,showFunc)
    delete_handler = get_handler('delete', delete, deleteFunc)
    add_handler = get_handler('add', add, addFunc)
    
    redact_handler = ConversationHandler(
        entry_points=[CommandHandler('redact', redact)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, redact_date)],
                2: [MessageHandler(Filters.text & ~Filters.command, redactFunc)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)

    stop_handler = CommandHandler('stop', stop)
    dp.add_handler(stop_handler)

    dp.add_handler(showall_handler)
    dp.add_handler(find_handler)
    dp.add_handler(show_handler)
    dp.add_handler(add_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(redact_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
