import telebot
from telebot import types
import datetime


bot = telebot.TeleBot('--- TOKEN ---')
avisos = []
enquete = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Iniciando projeto Skynet")


@bot.message_handler(commands=['add'])
def send_welcome(message):
    text = message.text.replace('/add', '')
    d = datetime.datetime.fromtimestamp(message.date).strftime('%d/%m/%Y, %Hh%Mmin')
    if text != '':
        avisos.append('[' + d + ']: ' + text)


@bot.message_handler(commands=['limpar'])
def limpar(message):
    del avisos[:]
    bot.send_message(message.chat.id, 'Quadro esvaziado')


@bot.message_handler(commands=['remover'])
def remover(message):
    check = True;
    n = message.text.replace('/remover', '')
    try:
        idx = int(n)
    except ValueError:
        check = False
    if idx <= len(avisos):
        check = False
    if check:
        avisos.pop(idx)
        bot.send_message(message.chat.id, 'Aviso ' + idx + ' removido.')
    else:
        bot.send_message(message.chat.id, 'Entrada invalida, tente entrar com o numero do aviso correto')


@bot.message_handler(commands=['board'])
def news_board(message):
    ans = '--- QUADRO DE NOTICIAS ---\n'
    if len(avisos) == 0:
        bot.send_message(message.chat.id, "Nada novo sob o sol de \'" + message.chat.title + "\'")
    else:
        for i in range(len(avisos)):
            ans = ans + str(i) + '.' + avisos[i] + '\n'
        bot.send_message(message.chat.id, ans)
bot.polling()
