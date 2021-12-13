import telebot
from telebot import types
bot = telebot.TeleBot('5019193840:AAEieVMgHMGItL2hmtbKHleqfcQJQdrwWNg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет.')
    elif message.text == 'Никнейм':
        bot.send_message(message.chat.id, f'Your Nik: {message.from_user.first_name}')
    elif message.text == 'ID':
        bot.send_message(message.from_user.id, f'Your ID: {message.from_user.id}')
    else:
        bot.send_message(message.from_user.id, 'напиши /help.')

@bot.message_handler(content_types=['text'])
def get_user_info(message):
    markup_infine = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data= 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data= 'no')

    markup_infine.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'тест кнопок',
        reply_markup = markup_infine
    )
@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('ID')
        item_username = types.KeyboardButton('НИКНЕЙМ')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'нажмите на одну из кнопок',
            reply_markup = markup_reply
        )

    elif call.data == 'no':
        pass


bot.polling(none_stop=True, interval=0)

