"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from datetime import datetime
import ephem

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

today = datetime.now()
planet_names = { 'Mars': ephem.Mars(today), 'Venus': ephem.Venus(today), 
'Saturn': ephem.Saturn(today),'Jupiter': ephem.Jupiter(today), 'Neptune': ephem.Neptune(today), 
'Uranus': ephem.Uranus(today), 'Mercury': ephem.Mercury(today) }

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_time(update, context):
  planet_name = update.message.text.split()[1]
  ephem_planet = planet_names.get(planet_name, None)
  if ephem_planet != None:
    constellation = ephem.constellation(planet_names[planet_name])
    update.message.reply_text(constellation[1])


def main():
    mybot = Updater("5467578606:AAGpSKASD5_ZKimvc2aBpaLCFgx1XLh9KBo", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_time))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
