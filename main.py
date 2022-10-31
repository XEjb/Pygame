import telebot

bot = telebot.TeleBot('5457216018:AAHtHe5l0jY78oPK8sVGVb7FDOt6JJ9kgzY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>hi dude</b>', parse_mode='html')


bot.polling(none_stop=True)