# Импортируем необходимые классы.
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application
from telegram.ext import CommandHandler
import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s - msg',
                    level=logging.INFO,
                    filename='bot.log')

reply_keyboard_1 = [['/portfolio', '/tutorials'], ['/version', '/weather']]
portfolio_keyboard_1 = [['/lastwork', '/allworks'], ['/back']]
tutorials_keyboard_1 = [['/anim_rig', '/vfx'], ['/back']]

markup_main = ReplyKeyboardMarkup(reply_keyboard_1, one_time_keyboard=False)
markup_portfolio = ReplyKeyboardMarkup(portfolio_keyboard_1, one_time_keyboard=False)
markup_tutorials = ReplyKeyboardMarkup(tutorials_keyboard_1, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "start",
        reply_markup=markup_main
    )
    log(update.effective_chat.id, '/start')


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )
    log(update.effective_chat.id, '/close_keyboard')


async def help(update, context):
    await update.message.reply_text(
        "Я бот 3D приколов. \nВот список команд: "
        "\n/weather - Погода в Амстердаме, где распологается офис Blender. "
        "\n/version - Последняя стабильная версия блендера и ссылка на ее скачивание"
        "\n/portfolio - Вам предложится выбор из двух команд: отправить последнюю или все работы"
        "\n/tutorials - Пара плейлистов с полезными туториалами (На клавиатуре можете выбрать тип туториалов)")
    log(update.effective_chat.id, '/help')


async def portfolio(update, context):
    await update.message.reply_text(
        "Последнюю работу или список всех?",
        reply_markup=markup_portfolio
    )
    log(update.effective_chat.id, '/portfolio')


async def tutorials(update, context):
    await update.message.reply_text(
        "Туториал на какую тему?",
        reply_markup=markup_tutorials
    )
    log(update.effective_chat.id, '/tutorials')


async def back(update, context):
    await update.message.reply_text(
        "Ну лан",
        reply_markup=markup_main
    )
    log(update.effective_chat.id, '/back')


async def allworks(update, context):
    r = requests.get('https://teletype.in/@haskie1337')
    html_text = r.text
    soup = BeautifulSoup(html_text, "html.parser")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    titles = []
    for title in soup.find_all("h2"):
        titles.append(title.text)

    for i in range(len(titles)):
        # print(titles[i], links[i + 4])
        await update.effective_message.reply_text(
            f"{titles[i]} {links[i + 4]}")
    log(update.effective_chat.id, '/allworks')


async def lastwork(update, context):
    r = requests.get('https://teletype.in/@haskie1337')
    html_text = r.text
    soup = BeautifulSoup(html_text, "html.parser")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    titles = []
    for title in soup.find_all("h2"):
        titles.append(title.text)

    await update.effective_message.reply_text(
        f"{titles[0]} {links[4]}")

    log(update.effective_chat.id, '/lastwork')


async def vfx(update, context):
    await update.effective_message.reply_text(
        "https://www.youtube.com/playlist?list=PLlV0HYg1k1bbHtdLmZ2oGXNnNiltEXslu")

    log(update.effective_chat.id, '/vfx')


async def anim_rig(update, context):
    await update.effective_message.reply_text(
        "https://www.youtube.com/playlist?list=PLlV0HYg1k1bboAY1EYVGhVR5wFM7TeAHQ")
    log(update.effective_chat.id, '/anim_rig')


async def version(update, context):
    r = requests.get('https://www.blender.org/')
    html_text = r.text

    soup = BeautifulSoup(html_text, "html.parser")
    res = soup.h1.string
    fin = str(res)

    await update.effective_message.reply_text(f"{fin} https://www.blender.org/download/")
    log(update.effective_chat.id, '/version')


async def weather(update, context):
    api_key = '34b2171f38964576c1143b464188c3dd'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Amsterdam&units=metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather_status = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

    await update.effective_message.reply_text(
        f"The weather in Amsterdam is: {weather_status} \nThe temperature in Amsterdam is: {temp}ºF")
    log(update.effective_chat.id, '/weather')


def main():
    logging.info('Start bot')
    application = Application.builder().token('6183612921:AAEa4L3XU2XWK3q3T5oL_54z5Vlc62IMze0').build()
    application.add_handler(CommandHandler("portfolio", portfolio))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("allworks", allworks))
    application.add_handler(CommandHandler("tutorials", tutorials))
    application.add_handler(CommandHandler("vfx", vfx))
    application.add_handler(CommandHandler("anim_rig", anim_rig))
    application.add_handler(CommandHandler("version", version))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("lastwork", lastwork))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


def log(user_id, msg):
    currentTime = datetime.now()
    with open(f'C:\logs\{user_id}.log', 'a+') as file:
        file.write(f'{currentTime} : {msg}\n')


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
