import telebot
from telebot import types

bot = telebot.TeleBot('нидам')

@bot.message_handler(commands=['start'])
def welcome(message):  
        #bot.reply_to(message, message.text)
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Понедельник")
        button2 = types.KeyboardButton("Вторник")
        button3 = types.KeyboardButton("Среда")
        button4 = types.KeyboardButton("Четверг")
        button5 = types.KeyboardButton("Пятница")
        
        menu.add(button1,button2, button3, button4, button5)
        bot.send_message(message.chat.id, "Привет, {0.first_name}, я могу показывать расписание, но его пока нет".format(message.from_user))
        bot.send_message(message.chat.id, "Выбери день недели.", reply_markup=menu)

@bot.message_handler(commands=['help'])
def helping(message):
        bot.send_message(message.chat.id, "Этот бот предназначен для вывода расписания")  

@bot.message_handler(content_types=['voice'])
def welcome2(message):
        bot.send_message(message.chat.id, "Учись печатать")

@bot.message_handler(content_types=['photo', 'document'])
def welcome3(message):
        bot.send_message(message.chat.id, "У меня памяти мало, не надо")

@bot.message_handler(content_types=['sticker'])
def welcome4(message):
        bot.send_message(message.chat.id, "БАН")

@bot.message_handler(content_types=['text'])
def get_messages(message):
        if message.chat.type == 'private':
                if (message.text.lower() == 'понедельник'):
                        bot.send_message(message.chat.id, '1. Обществознание \n2. Не помню')
                elif (message.text.lower() == 'вторник'):
                        bot.send_message(message.chat.id, '1. Информатика \n2. Алгебра')
                elif (message.text.lower() == 'среда'):
                        bot.send_message(message.chat.id, '1. Английский язык \n2. Литература')
                elif (message.text.lower() == 'четверг'):
                        bot.send_message(message.chat.id, '1. География \n2. РОДНОЙ русский')
                elif (message.text.lower() == 'пятница'):
                        bot.send_message(message.chat.id, '1. Математика \n2. И снова математика')
                else: 
                        bot.send_message(message.chat.id, 'Выбери день недели')


                


        
bot.polling(none_stop=True)
#while True:
        #try:
                #bot.polling(none_stop=True)
        #except Exception as e:
                #print(e)
                #bot.polling(none_stop=True)