# Импортируем необходимые классы.
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application
# Добавим необходимый объект из модуля telegram.ext
from telegram.ext import CommandHandler
import time

# from tokens import TG_TOKEN

# разметка клавиатуры
# Если передать все четыре строчки в виде одного списка,
# то получим клавиатуру с четырьмя кнопками в одну строку
reply_keyboard_1 = [['/dice', '/timer']]
dice_keyboard_1 = [['/one 6-edge cube', '/two 6-edge cubes'], ["/20-edge cube", '/back']]
timer_keyboard_1 = [['/30 sec', '/1 minute'], ['/5 minutes', '/back']]

# Параметр one_time_keyboard указывает,
# нужно ли скрыть клавиатуру после нажатия на одну из кнопок
markup_main = ReplyKeyboardMarkup(reply_keyboard_1, one_time_keyboard=False)
markup_dice = ReplyKeyboardMarkup(dice_keyboard_1, one_time_keyboard=False)
markup_timer = ReplyKeyboardMarkup(timer_keyboard_1, one_time_keyboard=False)


# Для того чтобы клавиатура появилась в диалоге у пользователя,
# необходимо добавить ее в качестве параметра reply_markup в функцию reply_text
async def start(update, context):
    await update.message.reply_text(
        "Я бот-лудоман. Что вам нужно?",
        reply_markup=markup_main
    )


# Переданная однажды клавиатура будет оставаться в диалоге в свернутом или развернутом виде до тех пор,
# пока клиенту не перешлют новую или не укажут явно, что клавиатуру надо удалить.
# Для удаления нужно в качестве значения параметра reply_markup передать
# объект специального класса: ReplyKeyboardRemove
async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def help(update, context):
    await update.message.reply_text(
        "Я бот лудоман, я умею бросать кубики и засекать таймеры!.")


async def dice(update, context):
    await update.message.reply_text(
        "Какой кубик(и) хотите бросить?",
        reply_markup=markup_dice
    )


async def back(update, context):
    await update.message.reply_text(
        "Ну лан",
        reply_markup=markup_main
    )


async def timer(update, context):
    await update.message.reply_text(
        "Сколько времени хотите засечь?",
        reply_markup=markup_main
    )


async def sec30(update, context):
    await update.message.reply_text(
        "Время работы: круглосуточно.")


def main():
    application = Application.builder().token('6183612921:AAEa4L3XU2XWK3q3T5oL_54z5Vlc62IMze0').build()
    application.add_handler(CommandHandler("dice", dice))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("timer", timer))
    application.add_handler(CommandHandler("30 sec", sec30))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
