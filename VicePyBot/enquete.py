@bot.message_handler(commands=['enquete'])
def enq(message):
    type = message.text.split()[1]
    if type == 'create':
        create(message)
    elif type == 'show':
        showEnquete(message)
    elif type == 'vote':
        #implementar
    else:
        bot.send_message(message.chat.id, 'Comando nao reconhecido, insira um comando valido.')

def create(message):
    markup = types.ForceReply()
    msg = bot.reply_to(message, 'Tópico da enquete?', reply_markup = markup)
    del enquete[:]
    enquete.append('--- ' + msg.text + ' ---\n')
    bot.register_next_step_handler(msg, entries)

def entries(message):
    markup = types.ForceReply()
    while True:
        msg = bot.reply_to(message, 'Adicionar opçao na enquete? (Digite -1 caso nao queira)', reply_markup = markup)
        if msg == -1:
            bot.send_message(message.chat.id, 'Enquete criada com sucesso!')
            break
        else:
            enquete.append(msg.text)

def showEnquete(message):
    if len(enquete) == 0:
        bot.send_message(message.chat.id, 'Sem enquetes no momento...')
    else:
        ans = ''
        for i in range(len(enquete)):
            ans += str(i) + '.' + enquete[i] + '\n'
        bot.send_message(message.chat.id, ans)
