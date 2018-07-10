@bot.message_handler(commands=['enquete'])
def enq(message):
    type = message.text.split()[1]
    if type == 'create':
        create(message)
    elif type == 'add_option':
        entries(message)
    elif type == 'show':
        showEnquete(message)
    elif type == 'vote':
        votar(message)
    elif type == 'end':
        encerrar(message)
    else:
        bot.send_message(message.chat.id, 'Comando nao reconhecido, insira um comando valido.')

def create(message):
    markup = types.ForceReply()
    msg = bot.reply_to(message, 'Tópico da enquete?', reply_markup = markup)
    del enquete[:]
    enquete.append('--- ' + msg.text + ' ---\n')

def entries(message):
    if len(enquete) == 0:
        ans = 'Sem enquete criada'
    else:
        markup = types.ForceReply()
        msg = bot.reply_to(message, 'What do you want?', reply_markup = markup)
        enquete.append(msg.text)
        ans = 'Adicionado com sucesso!'
        results.append(0)
    bot.send_message(message.chat.id, ans)

def votar(message):
    markup = types.ForceReply()
    msg = bot.reply_to(message, 'Vote limpo', reply_markup=markup)
    try:
        idx = int(msg.text)
        if idx >= len(enquete):
            results[idx] += 1
            ans = 'Voto na opção ' + str(idx) + ' adicionado com sucesso'
        else:
            ans = 'Opção invalida'

    except ValueError:
        ans = 'Opção invalida'
    bot.send_message(message.chat.id, ans)

def encerrar(message):
    if len(enquete) == 0:
        ans = 'Sem enquete ativa.'
    else:
        ans = '-- Competidores! -- \n'
        ans += opcoes()
        ans = '-- RESULTADO FINAL -- \n'
        ans += resultado()
    bot.send_message(message.chat.id, ans)



def resultado():
    ans = ''
    for i in range(len(results)):
        ans += str(i) + '.' + str(results) + ' votos\n'
    return ans

def opcoes():
    ans = ''
    for i in range(len(enquete)):
        ans += str(i) + '.' + enquete[i] + '\n'
    return ans
    

def showEnquete(message):
    if len(enquete) == 0:
        ans = 'Sem enquetes no momento...'
    else:
        ans = opcoes()
        ans += '--Resultado parcial--\n'
        ans += resultado()
    bot.send_message(message.chat.id, ans)
