from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tokens import bot_token
import logging, datetime
import ephem
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

answer = {"привет": "И тебе привет!", "как дела?": "Лучше всех", "пока": "Увидимся"}
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Yranus', 'Neptune']
planets = {'Mercury': ephem.Mercury,
           'Venus': ephem.Venus,
           'Mars': ephem.Mars,
           'Jupiter': ephem.Jupiter,
           'Saturn': ephem.Saturn,
           'Neptune': ephem.Neptune
           }


def greet_user(bot, update):
    text = 'Вызван /start'
    print(update)
    print(text)
    update.message.reply_text(text)


def planet(bot, update):
    text = 'Чтобы узнать местонахождение планеты, введите её название латинскими буквами'
    print(update)
    print(text)
    update.message.reply_text(text)

def planet_location(bot, update):
    date = datetime.datetime.now()
    date_now = date.strftime('%d.%m.%Y')
    question = update.message.text
    if question in planets:
        planet = planets[question](date_now)
        print(planet)
        location = ephem.constellation(planet)
        update.message.reply_text(location)


def wordcount(bot, update):
    quest = update.message.text
    quest2 = quest.replace("/wordcount ", "")
    count = quest2.split()
    if not count[-1].endswith('"') or not count[0].startswith('"'):
        update.message.reply_text("Введите текст в ковычках")
    else:
        update.message.reply_text(len(count))


def calc(bot, update):
    quest = update.message.text
    if quest.endswith('='):
        question = quest.replace('=', '')
        if "+" in question:
            count = question.split("+")
            qwe = (int(count[0]) + int(count[1]))
            update.message.reply_text(qwe)
        elif "-" in question:
            count = question.split("-")
            qwe = (int(count[0]) - int(count[1]))
            update.message.reply_text(qwe)
        elif "*" in question:
            count = question.split("*")
            qwe = (int(count[0]) * int(count[1]))
            update.message.reply_text(qwe)
        elif "/" in question:
            count = question.split("/")
            qwe = (int(count[0]) / int(count[1]))
            update.message.reply_text(qwe)
    else:
        update.message.reply_text("А не забыт ли знак '=' ?")



def calc_keyboard(bot, update):
    chat_id = update.message.chat_id
    custom_keyboard = [['1', '2', '3', '+'],
                       ['4', '5', '6', '-'],
                       ['7', '8', '9', '/'],
                       ['=', '0', '.', '*']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)


def talk_to_me(bot, update):
    question = update.message.text
    print(question)
    if question in answer:
        update.message.reply_text(answer[question])
    elif question in planets:
        planet_location(bot, update)
    else:
        wordcount(bot, update)
    #     question = update.message.text
    #     count = question.split()
    #     update.message.reply_text(len(count))
    #     # update.message.reply_text("Ну здрасте")


def main(token = bot_token):
    updater = Updater(str(token))

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calc", calc_keyboard))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, calc))


    updater.start_polling()
    updater.idle()


main()
