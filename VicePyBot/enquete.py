@bot.message_handler(commands=['enquete'])
def enq(message):
    select = message.text.split()
    try:
        tipo = select[1]
    except Exception as e:
        bot.send_message(message.chat.id, 'ERROOOU')
        return
    if tipo == 'create':
        try:
            zerotwo = select[2]
            enquete.append(zerotwo)
        except Exception as e:
            bot.send_message(message.chat.id, 'ERROOOU')
    elif tipo == 'add_option':
        try:
            zerotwo = select[2]
            entries(message, zerotwo)
        except Exception as e:
            bot.send_message(message.chat.id, 'ERROOOU')
    elif tipo == 'show':
        showEnquete(message)
    elif tipo == 'vote':
        try:
            zerotwo = select[2]
            votar(message, zerotwo)
        except Exception as e:
            bot.send_message(message.chat.id, 'ERROOOU')
    elif select[1] == 'end':
        encerrar(message)
    else:
        bot.send_message(message.chat.id, 'Comando nao reconhecido, insira um comando valido.')

def entries(message, s):
    if len(enquete) == 0:
        ans = 'Sem enquete criada'
    else:
        enquete.append(s)
        ans = 'Adicionado com sucesso!'
        results.append(0)
    bot.send_message(message.chat.id, ans)

def votar(message, idx):
    ans = ''
    try:
        idx = int(idx)
        if idx < len(results):
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
        ans = '--- Opções --- \n'
        ans += opcoes()
        ans += '-- RESULTADO FINAL -- \n'
        ans += resultado()
        del results[:]
        del enquete[:]
    bot.send_message(message.chat.id, ans)



def resultado():
    ans = ''
    for i in range(len(results)):
        ans += enquete[i + 1] + '. ' + str(results[i]) + ' votos\n'
    return ans

def opcoes():
    ans = ''
    for i in range(1, len(enquete)):
        ans += str(i) + '.' + enquete[i] + '\n'
    return ans


def showEnquete(message):
    if len(enquete) == 0:
        ans = 'Sem enquetes no momento...'
    else:
        ans = '--- ' + enquete[0] + ' ---\n'
        ans = opcoes()
        ans += '\n---Resultado parcial---\n'
        ans += resultado()
    bot.send_message(message.chat.id, ans)
