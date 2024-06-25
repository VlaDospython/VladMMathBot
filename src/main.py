import os
import telebot
from controller import Controller

print(help(telebot))

# My name is VLAD_M_TELEGRAM_BOT_1_TOKEN
token = os.environ['VLAD_M_TELEGRAM_BOT_1_TOKEN']
bot = telebot.TeleBot(token, parse_mode='MarkdownV2')
controller = Controller(bot)

welcome_text1, welcome_text2 = "Вітаю, це Telegram бот, який", "перевіряє твої знання з математики\\!"
help_text = "Бот надсилає питання та варіанти відповіді. У ботові тільки тести. Користувач повинен сам ввести *А Б В Г Д*. Бот перевіряє, чи відповідь правильна. Якщо відповідь правильна, бот вітає користувача з правильною відповіддю. "


@bot.message_handler(func=lambda message: True)
def command(message):
    controller.handle_text(message.text, message.chat.id)


if __name__ == '__main__':
    bot.infinity_polling()


# /start - Бот вітається та розповідає, як із ним працювати
# /help - Бот розповідає, як ним користуватися
# /answer - Якщо було надіслано питання, то бот одразу дає правильну відповідь на це питання. Під час використання цієї команди бали не додаються.
# /next - Надіслати наступне питання
# /stat - Статистика про те, скільки тестів було пройдено і у скількох тестах була дана правильна відповідь.
# /reset - Почати проходити тест заново. Занулити бали.
# /feedback - Дозволяє користувачу написати відгук про користування ботом: сподобалося йому чи ні, які враження та побажання