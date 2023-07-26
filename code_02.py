import random
import telebot

# Токен вашего бота, полученный от BotFather
TOKEN = '6611500225:AAEba0FjSIrsJsfARHVAKut1NUrZQ1gTVq8'

# Список вопросов и ответов для игры
questions = {
    "Какой газ является основным компонентом воздуха?": ["Кислород", "Азот", "Углекислый газ", "Водород"],
    "Какая самая большая планета в Солнечной системе?": ["Юпитер", "Марс", "Венера", "Сатурн"],
    "Какой город является столицей Италии?": ["Рим", "Милан", "Неаполь", "Турин"],
    "Кто написал роман 'Война и мир'?": ["Лев Толстой", "Федор Достоевский", "Александр Пушкин", "Михаил Лермонтов"]
}

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в игру 'Кто хочет стать миллионером'!")
    bot.send_message(message.chat.id, "Ответьте на все вопросы правильно, чтобы выиграть миллион!")

    # Запуск игры
    start_game(message.chat.id)


# Функция для задания вопроса и проверки ответа
def ask_question(chat_id):
    question = random.choice(list(questions.keys()))
    correct_answer = questions[question][0]
    answers = questions[question]
    random.shuffle(answers)

    question_text = f"{question}\n\n"
    for i, answer in enumerate(answers):
        question_text += f"{i + 1}. {answer}\n"

    bot.send_message(chat_id, question_text)

    # Функция-обработчик ответа пользователя
    @bot.message_handler(func=lambda message: message.chat.id == chat_id)
    def check_answer(message):
        if message.text.isdigit() and 1 <= int(message.text) <= len(answers):
            selected_answer = answers[int(message.text) - 1]
            if selected_answer == correct_answer:
                bot.send_message(chat_id, "Правильный ответ!")
                start_game(chat_id)  # Переход к следующему вопросу
            else:
                bot.send_message(chat_id, "Неправильный ответ! Игра окончена.")
        else:
            bot.send_message(chat_id, "Некорректный ввод! Пожалуйста, введите номер правильного ответа.")


# Функция для запуска игры
def start_game(chat_id):
    if len(questions) > 0:
        ask_question(chat_id)
    else:
        bot.send_message(chat_id, "Поздравляю! Вы выиграли миллион!")


# Запуск бота
bot.polling()
