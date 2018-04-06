import telebot

bot  = telebot.TeleBot('--- TOKEN HERE ---')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Pois não?")

@bot.message_handler(commands=['sino'])
def send_welcome(message):
    bot.reply_to(message, "Olá Mestre")

@bot.message_handler(func=lambda m: True)
def gago_analizer(message):
    if message.text == 'sou gago':
        if message.from_user.username == 'ligre17':    
            bot.reply_to(message, "aí é verdade, pelo menos por enquanto....")
        else:
            bot.reply_to(message, "mentira")
    if(message.text.find("foda-se")!=-1):
        bot.send_message(message.chat.id, "Meça suas palavras")

bot.polling()
