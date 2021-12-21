import requests
import telebot
from telebot import types
token = '5019193840:AAEieVMgHMGItL2hmtbKHleqfcQJQdrwWNg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('История поездок')
    item2 = types.KeyboardButton('Ближайший самокат')
    item3 = types.KeyboardButton('Информация')
    markup.add(item1, item2, item3)
    bot.send_message(m.chat.id, 'Приветствую тебя, {0.first_name}!, я информационный бот. \n Для получения информации можете воспользоваться подсказками ниже'.format(m.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def phone(m, res = False):
    if m.chat.type == 'private':
        if m.text == 'История поездок':

            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_phone = types.KeyboardButton(text='Узнать историю поездки', request_contact=True)
            keyboard.add(button_phone)
            bot.send_message(m.chat.id, 'Поделитесь контактом чтоб посмотреть свою историю поездки', reply_markup=keyboard)
        elif m.text == 'Ближайший самокат':
            pass
        elif m.text == 'Информация':
            pass
        elif m.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('История поездок')
            item2 = types.KeyboardButton('Ближайший самокат')
            item3 = types.KeyboardButton('Информация')
            markup.add(item1, item2, item3)
            bot.send_message(m.chat.id, '', reply_markup= markup)




@bot.message_handler(content_types=['text'])
def get_user_info(message):
    if message.text == "тест":
        markup_infine = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data= 'yes')
        item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data= 'no')

        markup_infine.add(item_yes, item_no)
        bot.send_message(message.chat.id, 'тест кнопок',
        reply_markup = markup_infine)
@bot.callback_query_handler(func= lambda call: True)
def answer(call):
        if call.data == 'yes':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_id = types.KeyboardButton('ID')
            item_username = types.KeyboardButton('Никнейм')

            markup_reply.add(item_id, item_username)
            bot.send_message(call.message.chat.id, 'нажмите на одну из кнопок',
            reply_markup = markup_reply
)

        elif call.data == 'no':
            pass












#Модуль история поездок



@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        print(message.contact)
        pol = '+' + message.contact.phone_number
    def history():
        phn = {'phone': pol}
        url = 'https://uram.ddns.net/uram_bot/history'
        req_j = requests.post(url, json=phn)
        req_data = req_j.json()
        if req_j.status_code == 200:
            try:
                for req_data['history'][0] in req_data['history']:
                    bot.send_message(message.from_user.id, 'Цена: ' + str(req_data['history'][0]['cost']) +
                '\nНачало: ' + req_data['history'][0]['start_time'] +
                '\nКонец: ' + req_data['history'][0]['end_time'] +
                '\nСтатус поездки: ' + req_data['history'][0]['status'])
                req_data['history'][+1]
            except KeyError:
                print('Что то пошло не так')
            except IndexError:
                print()
        else:
            print('Что то пошло не так')
    t = history()











print('bot started')
bot.polling(none_stop=True, interval=0)