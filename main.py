import telebot

bot = telebot.TeleBot('5457216018:AAHtHe5l0jY78oPK8sVGVb7FDOt6JJ9kgzY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)