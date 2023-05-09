import telebot
from telebot import types
#инициализируем бота:
API_Token = "6012439320:AAFtduiAl2VTvNkI7y8rrPES9WZkz_YbfDo"
bot = telebot.TeleBot(API_Token)

#text = 'https://mtuci.ru/upload/iblock/6d5/w1ka4v2osqwpfsoqtymayrfdoqe8r07b/BIK2102.pdf'
""""@bot.message_handler(regexp = '1')
def d(message):

    current_chat_id = message.chat.id
    bot.send_message(chat_id=current_chat_id, text=type(message))


def func(message):
    t = message.text
    text = f'https://mtuci.ru/upload/iblock/6d5/w1ka4v2osqwpfsoqtymayrfdoqe8r07b/{t}.pdf'
    current_chat_id = message.chat.id
    bot.send_message(chat_id=current_chat_id, text= text)
@bot.message_handler(regexp = '2')
#@bot.message_handler(content_type = 'text')
def d(message):
    current_chat_id = message.chat.id
    bot.send_message(chat_id=current_chat_id, text='ghjk')
    bot.register_next_step_handler(message, func)

bot.infinity_polling()"""

""""@bot.message_handler(commands = ['start'])
def send_welcome(message):
    current_chat_id = message.chat.id
    bot.send_message(chat_id = current_chat_id, text = 'Приветствую!')
    bot.send_message(chat_id=current_chat_id , text = 'fghjk')
    markup = types.ReplyKeyboardMarkup(row_width = 1)
    btn1 = types.KeyboardButton('Расписание')
    btn2 = types.KeyboardButton('Полезная информация')
    btn3 = types.KeyboardButton('Для старосты')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup= markup)
"""
pr_chat_id = 'fghj'
def func2(message):
    bot.send_message(chat_id = message.chat.id, text = pr_chat_id)


@bot.message_handler(content_types = ['text'])
def f(message):
    bot.send_message(chat_id=message.chat.id, text='Опубликуйте сообщение для всех пользователей:')
    pr_chat_id = message.chat.id
    bot.register_next_step_handler(message, func2)
bot.infinity_polling()