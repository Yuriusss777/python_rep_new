from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Список матных и ругательных слов
bad_words = ["блядь", "блять", "хуй", "нахуй", "пизда", "пиздец", "член"]


def start(update: Update, context) -> None:
    """Обработчик команды /start"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для проверки матных слов.")


def check_text(update: Update, context) -> None:
    """Обработчик текстовых сообщений"""
    message_text = update.message.text.lower()

    for word in bad_words:
        if word in message_text:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Обнаружено матное слово. Пожалуйста, будьте вежливы!")
            return


def main() -> None:
    """Основная функция"""
    # Токен вашего бота
    token = "5929644201:AAHMZPw03V-s7p7v-zAAVM-BEdm8GZtHl68"

    # Создание экземпляра Updater и передача токена
    updater = Updater(token=token, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрация обработчика текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), check_text))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
