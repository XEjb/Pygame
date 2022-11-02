import telebot

bot = telebot.TeleBot('5457216018:AAHtHe5l0jY78oPK8sVGVb7FDOt6JJ9kgzY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
    elif message.text == 'Спасибо':
        bot.send_message(message.chat.id, 'Всегда рад помочь', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('photo_2022-01-22_23-07-58.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю чувак", parse_mode='html')


bot.polling(none_stop=True)