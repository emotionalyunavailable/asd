import requests
import telebot
from telebot import types
bot = telebot.TeleBot('5019193840:AAEieVMgHMGItL2hmtbKHleqfcQJQdrwWNg')

@bot.message_handler(commands=['nummer'])
def phone(messages):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text='Send phone', request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(messages.chat.id, 'Nummer', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(messages):
    if messages.contact is not None:
        print(messages.contact)
        gol = '+' + messages.contact.phone_number
        global lose
        lose = gol

@bot.message_handler(commands=["geo"])
def geo(messages):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(messages.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(messages):
    if messages.location is not None:
        print(messages.location)
        print("latitude: %s; longitude: %s" % (messages.location.latitude, messages.location.longitude))
        def greting():
            url = 'https://uram.ddns.net/uram_bot/find'
            req = {'lat': '18', 'lon': '18'}
            data = messages.location.latitude
            data2 = messages.location.longitude
            req['lat'] = data
            req['lon'] = data2
            req['phone'] = lose
            req_j = requests.post(url, json=req)
            req_data = req_j.json()
            da = req_j.text
            a = req_data['lat']
            b = req_data['lon']
            print(a, b)
            global result
            result = a, b
        test = greting()

@bot.message_handler(content_types=['text'])
def get_text_messages(messages):
    if messages.text == 'Привет':
        bot.send_message(messages.from_user.id, 'Привет.')
    elif messages.text == '/help':
        bot.send_message(messages.from_user.id, 'Тебе нужно ввести команду /nummer, чтобы мы получили твой номер телефона, так же напиши /geo и отправь свое местоположение.')
    elif messages.text == 'Никнейм':
        bot.send_message(messages.chat.id, f'Your Nik: {messages.from_user.first_name}')
    elif messages.text == 'ID':
        bot.send_message(messages.from_user.id, f'Your ID: {messages.from_user.id}')
    elif messages.text == 'Нефтекамск':
        print(result)
        longitude = result[1]
        latitude = result[0]
        bot.send_location(messages.from_user.id, latitude, longitude)
    else:
        bot.send_message(messages.from_user.id, 'напиши /help.')


@bot.message_handler(content_types=['text'])
def get_user_info(messages):
    markup_infine = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data= 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data= 'no')

    markup_infine.add(item_yes, item_no)
    bot.send_message(messages.chat.id, 'тест кнопок',
        reply_markup = markup_infine
    )
@bot.callback_query_handler(func= lambda call: True)
def answer(calls):
    if calls.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('ID')
        item_username = types.KeyboardButton('Никнейм')

        markup_reply.add(item_id, item_username)
        bot.send_message(calls.message.chat.id, 'нажмите на одну из кнопок',
            reply_markup = markup_reply
        )

    elif calls.data == 'no':
        pass

print('bot started')
bot.polling(none_stop=True, interval=0)
