import telebot

# экземпляр бота
bot = telebot.TeleBot('5556955592:AAFo7CxuSkQXulBK2X_egAjl9j7hNzgeuyo')


# start button
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Привет! С чего начнём?")


# getteing user's messeges
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)
