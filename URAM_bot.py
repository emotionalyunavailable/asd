import telebot
bot = telebot.TeleBot('5019193840:AAEieVMgHMGItL2hmtbKHleqfcQJQdrwWNg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет .')
    else:
        bot.send_message(message.from_user.id, 'напиши /help.')


bot.polling(none_stop=True, interval=0)
