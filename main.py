"""TODO: 1. Расписание(общее, экзаменов)
         2. Полезная информация (неделя, дз, фио преподавателя?, курсовые примеры)
         3. ?рассылка общих сообщений от старосты?
"""
#tb.forward_message(to_chat_id, from_chat_id, message_id)
import telebot
import pandas as pd
import requests
from telebot import types

#инициализируем бота:
API_Token = "6012439320:AAFtduiAl2VTvNkI7y8rrPES9WZkz_YbfDo"
bot = telebot.TeleBot(API_Token)

#типовые фразы
alph = [
    "Вот что может этот бот:\n1.  Показать расписание (полное расписание занятий, расписание за определённый день недели, расписание экзаменов\n2. Ответы на типовые вопросы (см раздел вопросы)\n Чтобы вызвать подсказку ещё раз напишите /help\n"

]

chat_id = []
#считываем расписание:
def time_table(group):
    exel_file = pd.ExcelFile(f'D:\Desktop\Программы Питон\ИТИП_bot\data\{group}.xlsx')
    df = pd.read_excel(exel_file)
    col_names = [
        'day',
        'l_num',
        'l_time',
        'l_room_1',
        'l_type_1',
        'lector_1',
        'discipline_1',
        'discipline_2',
        'lector_2',
        'l_type_2',
        'l_room_2'
    ]
    df.columns = col_names
    indexes = list(df.columns)
    indexes[:len(col_names)] = col_names
    df.columns = indexes
    norm_t_table = df[df['l_time'].notna()].copy()
    norm_t_table.dropna(
        axis=1,
        how='all',
        inplace=True
    )
    norm_t_table['day'] = norm_t_table['day'].ffill()
    col_to_drop = [col for col in norm_t_table.columns if col not in col_names]
    norm_t_table.drop(
        columns=col_to_drop,
        inplace=True
    )
    norm_t_table.drop(
        norm_t_table[norm_t_table['day'] == 'День недели'].index,
        inplace=True
    )
    rows = norm_t_table[norm_t_table['l_room_1'].isnull() == True]
    rows = rows[norm_t_table['l_room_2'].isnull() == True]
    norm_t_table.drop(
        index = rows.index,
        inplace = True
    )
    return norm_t_table


group = 'BIK2102'
#time_t = time_table(group)
#time_t.to_excel('D:\Desktop\Программы Питон\ИТИП_bot\data\output.xlsx')
#print(time_t)

password = '12345'
r = 0
p = 0
pr_chat_id = 'dfgh'
def func2(message):
    for i in range(len(chat_id)):
        I = 0

def func1(message):
    password = message.text
    return None
def func0(message):
    t = message.text
    text = f'https://mtuci.ru/upload/iblock/6d5/w1ka4v2osqwpfsoqtymayrfdoqe8r07b/{t}.pdf'
    bot.send_message(chat_id = message.chat.id, text = text)
def func(message):
    try:
        t = message.text
        #df = time_table(group)
        #df.to_excel(f'D:\Desktop\Программы Питон\ИТИП_bot\data\{group}.xlsx')
        doc = open(f'D:\Desktop\Программы Питон\ИТИП_bot\data\{t}.xlsx', 'rb')
        current_chat_id = message.chat.id
        bot.send_document(chat_id = current_chat_id, document = doc)
    except: bot.send_message(chat_id = message.chat.id, text = 'Неверно введён номер группы или таокй группы нет в нашей базе данных, пожалуйста попробуйте снова')

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    chat_id.append(message.chat.id)
    current_chat_id = message.chat.id
    bot.send_message(chat_id = current_chat_id, text = 'Приветствую!')
    bot.send_message(chat_id=current_chat_id , text = alph[0])
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Расписание')
    btn2 = types.KeyboardButton('Полезная информация')
    btn3 = types.KeyboardButton('Кто лучший преподаватель и поставит нам зачёт?')
    #btn3 = types.KeyboardButton('Для старосты')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands = ['help', 'back'])
def send_help(message):
    current_chat_id = message.chat.id
    bot.send_message(chat_id=current_chat_id, text = alph[0])
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Расписание')
    btn2 = types.KeyboardButton('Полезная информация')
    #btn3 = types.KeyboardButton('Для старосты')
    btn3 = types.KeyboardButton('Кто лучший преподаватель и поставит нам зачёт?')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

r =0
@bot.message_handler(content_types = ['text'])
def ans(message):
    current_chat_id = message.chat.id
    if message.text == 'Кто лучший преподаватель и поставит нам зачёт?':
        bot.send_message(message.chat.id, text = 'Кончно же Дмитрий Аркадьевич Егоров!!!')
    if message.text == 'Расписание':
        bot.send_message(chat_id=current_chat_id, text='Введите вашу группу на латинице (пример: BIK2102)')
        bot.send_message(chat_id=current_chat_id, text='К сожалению  в данный момент, из-за того что в отделе расписания работают тупые гандоны, которые не могут сделать ничего полезного, сервис не работает на полную мощность и выдаёт старые расписания. Спасибо за понимание!') #Мы можем предложить вам загрузить файл  с вашим расписанием, который мы запомним и будем по нему выдавать вам информацию. Пожалуйста загружайте только файлы с расписанием, другие могут сломать нашего бота! Спасибо за понимание!')
        bot.register_next_step_handler(message, func)
    if message.text == 'Полезная информация':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn4 = types.KeyboardButton('Номер недели')
        btn5 = types.KeyboardButton('Пример написания курсовой')
        btn6 = types.KeyboardButton('/back')
        markup.add(btn4, btn5, btn6)
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
    if message.text == 'Номер недели':
        k = 13
        bot.send_message(chat_id = message.chat.id, text = k)
        if k%2 ==  0:
            bot.send_message(chat_id = message.chat.id, text = 'Неделя чётная')
        elif k%2 != 0:
            bot.send_message(chat_id = message.chat.id, text = 'Неделя нечётная')
    if message.text == 'Пример написания курсовой':
        doc = open('D:\Desktop\Программы Питон\ИТИП_bot\data\Пример курсовой.docx', 'rb')
        bot.send_document(chat_id = message.chat.id, document = doc)
    """if message.text == 'Для старосты':
        bot.send_message(chat_id = message.chat.id, text = 'Введите пароль')
    if message.text == password:
        r = 1
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn7 = types.KeyboardButton('Изменить пароль')
        btn8 = types.KeyboardButton('Опубликовать сообщение')
        btn9 = types.KeyboardButton('/back')
        markup.add(btn7, btn8, btn9)
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
    if message.text == 'Изменить пароль' and r!=0:
        bot.register_next_step_handler(message, func1)
    elif r==0:
        bot.send_message(message.chat.id, text = 'Неверный пароль')
    if message.text == 'Опубликовать сообщение:' and r!=0:
        bot.send_message(chat_id = message.chat.id, text = 'Опубликуйте сообщение для всех пользователей:')
        pr_chat_id = message.chat.id
        bot.register_next_step_handler(message, func2(pr_chat_id))
    elif r==0 :
        bot.send_message(message.chat.id, text='Неверный пароль')"""





""""@bot.message_handler(content_types = ['document'])
def func(message):
    current_chat_id = message.chat.id
    bot.send_message(chat_id = current_chat_id,text = 'sdfghjkl;rtghyjklkiuytrfdsdfghjk' )
    f_id = message.document.file_id
    df = bot.get_file(file_id = f_id)
    #df.save('D:\Desktop\Программы Питон\ИТИП_bot\data')"""


bot.infinity_polling()