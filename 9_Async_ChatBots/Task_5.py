# Импортируем необходимые классы.
from telegram.ext import Application, MessageHandler, filters


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token('6183612921:AAEa4L3XU2XWK3q3T5oL_54z5Vlc62IMze0').build()

    text_handler = MessageHandler(filters.TEXT, echo)

    application.add_handler(text_handler)

    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
