# Импортируем необходимые классы.
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
import datetime


# async def echo(update, context):
#     await update.message.reply_text(update.message.text)


async def time(update, context):
    now = datetime.datetime.now()
    now.time()
    await update.message.reply_html(
        await update.message.reply_text("Текущее время: ", now.time())
    )


async def data(update, context):
    today = date.today()
    await update.message.reply_html(
        await update.message.reply_text("Текущая дата: ", today)
    )


def main():
    application = Application.builder().token('6183612921:AAEa4L3XU2XWK3q3T5oL_54z5Vlc62IMze0').build()
    # text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    # application.add_handler(text_handler)
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("date", data))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
