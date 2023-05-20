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
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import ephem
from datetime import datetime

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

planets_dict = {
    'Sun': lambda d: ephem.Sun(d),
    'Mercury': lambda d: ephem.Mercury(d),
    'Venus': lambda d: ephem.Venus(d),
    'Moon': lambda d: ephem.Moon(d),
    'Mars': lambda d: ephem.Mars(d),
    'Jupiter': lambda d: ephem.Jupiter(d),
    'Saturn': lambda d: ephem.Saturn(d),
    'Uranus': lambda d: ephem.Uranus(d),
    'Neptune': lambda d: ephem.Neptune(d),
    'Pluto': lambda d: ephem.Pluto(d),
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Вызван /start')
    await update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

async def handle_planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    parts = update.message.text.split()
    if len(parts) < 2:
      await update.message.reply_text('Не задана планета. Попробуйте: /planet Mars')
      return    
    planet_name = parts[1].strip()
    if not planet_name in planets_dict:
        await update.message.reply_text(f'Планета не найдена или не поддерживается. Поддерживаемые планеты: {[k for k in planets_dict.keys()]}')
        return

    today = datetime.today().strftime('%Y/%m/%d')
    planet = planets_dict[planet_name](today)
    constellation = ephem.constellation(planet)
    await update.message.reply_text(f'Planet {parts[1]} is in constellation: {constellation}')

def main():
    application = ApplicationBuilder().token(settings.API_KEY).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    planet_handler = CommandHandler("planet", handle_planet)
    application.add_handler(planet_handler)

    logging.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()
