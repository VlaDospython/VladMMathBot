from telebot import TeleBot


class Controller:
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def handle_text(self, text: str, chat_id: int):
        self.current_chat_id = chat_id
        match text:
            case "/start":
                self.__start()
            case _:
                self.__unknown_command()

    def __start(self):
        self.bot.send_message(self.current_chat_id,
                              "Вітаю, це Telegram бот, який перевіряє твої знання з математики\\!")

    def __unknown_command(self):
        self.bot.send_message(self.current_chat_id,
                              "Я вас не розумію")
        
        