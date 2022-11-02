import telebot
from telebot import types

bot = telebot.TeleBot('5457216018:AAHtHe5l0jY78oPK8sVGVb7FDOt6JJ9kgzY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
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


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'хахаха, ну и пикчерс. Удали, не позорься')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url='https://www.youtube.com/'))
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton("Start")

    markup.add(website, start)
    bot.send_message(message.chat.id, 'выберите действие', reply_markup=markup)


bot.polling(none_stop=True)