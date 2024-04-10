import telebot

class Mindmurt:
    # Constructor to initialize the object with name and age
    def __init__(self):
        print("creating Mindmurt...")
        self.runMindmurt()

    # Method to display information about the person
    def runMindmurt(self):
        bot = telebot.TeleBot('7031513468:AAG3B_TRgNDUjVA7IGW9RPlvwSvZC-YTPaY')
        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            # @bot.message_handler(content_types=['text', 'document', 'audio'])
            if message.text == "Привет":
                bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
            elif message.text == "/help":
                bot.send_message(message.from_user.id, "Напиши привет")
            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

        bot.polling(none_stop=True, interval=1)
