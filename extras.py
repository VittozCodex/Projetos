# bibliotecas personalizadas
import colors
import variables
# bibliotecas python
from os import name, system, path, remove, write
from platform import system as osname
from random import randint, choice
from time import sleep

cheatAtivo = False  # verifica se algum cheat foi ativado

def title():
    # mostra apenas o título do jogo
    if osname() == 'Windows':
        system('cls')
    elif osname() == 'Linux':
        system('clear')
    else:
        pass
    print(f'  {colors.cyan}===================={colors.reset}')
    print(f'{colors.cyan}======{colors.reset} {colors.white}O Tráfico{colors.reset} {colors.cyan}======={colors.reset}')
    print(f'  {colors.cyan}===================={colors.reset}\n')


def verificar():
    # função para verificações iniciais
    if variables.vezesPreso >= variables.maximoVezesPreso:
        # Caso atingir o limte de prisão
        title()
        print(f'{colors.red}Aviso:{colors.reset} Você pegou prisão perpétua. Fim de jogo.\n')
        exit()

    if variables.vezesPreso <= 0:
        # não está preso
        variables.saldoBloqueado = False
    elif variables.vezesPreso > variables.bloquearConta:
        # bloquear saldo bancário
        variables.saldoBloqueado = True

    if variables.chancePolicia > 100:
        # chances da polícia não pode passar de 100%
        variables.chancePolicia = 100
    if variables.chancePolicia < 1:
        # chances da polícia não pode ser nula
        variables.chancePolicia = 1

    if variables.chanceCorrer > 100:
        # chances de correr não pode passar de 100%
        variables.chanceCorrer = 100
    if variables.chanceCorrer < 1:
        # chances de correr não pode ser nula
        variables.chanceCorrer = 1

    if variables.money < 0:
        # o dinheiro não pode ficar negativo
        variables.money = 0

    if variables.chanceAssaltarBanco > 100:
        # as chances de assaltar o banco não pode passar de 100%
        variables.chanceAssaltarBanco = 100
    if variables.chanceAssaltarBanco < 1:
        # as chances de assaltar o banco não pode ser nula
        variables.chanceAssaltarBanco = 1

    if variables.chanceAssaltarPessoas > 100:
        # as chances de assaltar pessoas não pode passar de 100%
        variables.chanceAssaltarPessoas = 100
    if variables.chanceAssaltarPessoas < 1:
        # as chances de assaltar pessoas não pode ser nula
        variables.chanceAssaltarPessoas = 1

    if variables.devendoBanco <= 0:
        # resetar empréstimo caso não estiver devendo
        variables.emprestimoCheck = False


def verificar_nomes(nomeJogador, nomeDroga):
    # verifica e filtra os nomes iniciais
    if len(nomeJogador) <= 0:
        # se os dois nomes estiverem vazios
        print(f'\n{colors.red}Aviso:{colors.reset} O nome do traficante não pode ficar vazio.')
        input()
        return False
    elif len(nomeDroga) <= 0:
        # se o nome da droga estiver vazio
        variables.drugName = nome_droga()
        #input()
        return True
    else:
        # caso todos os nomes estejam preenchidos
        for i in nomeJogador:
            # verifica se tem espaço no nome do jogador
            if i == ' ':
                print(f'\n{colors.red}Aviso:{colors.reset} Não pode conter espaços no nome do jogador.')
                input()
                return False
        for g in nomeDroga:
            # verifica se tem espaço no nome da droga
            if g == ' ':
                print(f'\n{colors.red}Aviso:{colors.reset} Não pode conter espaços no nome da droga.')
                input()
                return False
        return True


def cheats(*args):
    # trapaças p/ desenvolvedor
    global cheatAtivo

    try:
        if args[0][0].lower() == '/help':
            title()
            print(f'{colors.yellow}Comandos/cheats\n{colors.reset}')
            print('/playername <nome>: Altera o nome do usuário\n')
            print('/drugname <nome>: Altera o nome da droga.\n')
            print('/drug <valor>: Altera a quantidade de drogas.\n')
            print('/money <valor>: Altera a quantidade de dinheiro.\n')
            print('/product <valor>: Altera a quantidade de drogas produzidas.\n')
            print('/timeproduct <valor>: Altera o tempo para produzir a droga.\n')
            print('/policedrug <valor>: Altera a chance da polícia aparecer ao vender as drogas.\n')
            print('/allupgrades: Ativa todos os upgrades.\n')
            print('/clearprisions: Limpar todas prisões.')
            print(f'\n{colors.red}Aviso:{colors.reset} Todos os comandos acima ativam o modo cheat.')
            input()
        elif args[0][0].lower() == '/money':
            variables.money = int(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/drug':
            variables.drug = int(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/disablecheatmode':
            if cheatAtivo == False:
                print('\nO modo cheat já está desativado.')
                input()
            else:
                cheatAtivo = False
        elif args[0][0].lower() == '/playername':
            variables.playerName = str(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/drugname':
            variables.drugName = str(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/product':
            variables.gramas = int(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/timeproduct':
            variables.tempoProduzirDrogas = int(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/policedrug':
            variables.chancePolicia = int(args[0][1])
            cheatAtivo = True
        elif args[0][0].lower() == '/save':
            save()
        elif args[0][0].lower() == '/allupgrades':
            variables.diminuirTempoProducaoCheck = True
            variables.aumentarMultiplicadorDeGanhosCheck = True
            variables.diminuirChanceCorrerDaPoliciaCheck = True
            cheatAtivo = True
        elif args[0][0].lower() == '/clearprisions':
            variables.foiPreso = False
            variables.vezesPreso = 0
            cheatAtivo = True
        else:
            print(f'\n{colors.red}Aviso:{colors.reset} Nenhum comando encontrado.')
            input()
    except Exception as erro:
        print(f'\nErro de comando. O modo {colors.red}cheat{colors.reset} foi ativado por tentativa.')
        cheatAtivo = True
        input()


def random_number():
    # retorna um número aleatório entre 1 e 100
    return randint(1, 101)


def gerar_drogas(quantidade_drogas):
    # função que retorna a quantidade de drogas que o cliente comprará
    return randint(1, quantidade_drogas)


def gerar_dinheiro(dinheiro_maximo):
    # retorna uma quantidade de dinheiro
    return randint(1, dinheiro_maximo)


def preso():
    # resetar tudo caso for preso
    variables.drug = 0
    variables.money = 0
    #variables.gramas = 10
    #variables.tempoProduzirDrogas = 3
    #variables.precoProducao = 500
    variables.vezesPreso = variables.vezesPreso + 1
    variables.foiPreso = True


def policia_drogas():
    # caso for pego pela polícia
    while True:
        title()

        print(f'{colors.red}Aviso:{colors.reset} A polícia te avistou vendendo drogas, o que quer fazer?')

        if variables.diminuirChanceCorrerDaPoliciaCheck:
            # comprou o upgrade
            print(f'\n{colors.blue}1.{colors.reset} Correr igual uma gazela [Chance: {colors.magenta}{variables.chanceCorrer}%{colors.reset}]')
        else:
            # não comprou o upgrade
            print(f'\n{colors.blue}1.{colors.reset} Correr igual uma gazela [Chance: {colors.yellow}{variables.chanceCorrer}%{colors.reset}]')

        print(f'\n{colors.blue}2.{colors.reset} Trocar tiro com a polícia [Chance: {colors.yellow}{variables.chanceTrocarTiro}%{colors.reset}]')
        print(f'\n{colors.blue}3.{colors.reset} Se entregar pacificamente [Fiança: {colors.yellow}R${variables.fianca}{colors.reset}]')

        option = str(input(f'\nOpção[{colors.blue}R${variables.money}{colors.reset}]: '))

        #title()
        #print(f'Vender Drogas [Polícia: {colors.red}{variables.chancePolicia}%{colors.reset}]')

        if option == '1':
            # correr
            if random_number() <= variables.chanceCorrer:
                print(f'\n{colors.green}Aviso:{colors.reset} Você fugiu da polícia correndo igual uma gazela.')
                input()
                break
            else:
                print(f'\n{colors.red}Aviso:{colors.reset} Você tentou fugir, mas a polícia o pegou. Você foi preso.')
                preso()
                input()
                break
        elif option == '2':
            # trocar tiros
            if random_number() <= variables.chanceTrocarTiro:
                # ganhou a troca de tiros
                print(f'\n{colors.green}Troca de tiros:{colors.reset} Você matou o polícial na troca de tiros e conseguiu fugir.')
                
                if variables.chancePolicia >= 100:
                    # caso as chances da polícia esteja maior ou igual a 100%
                    pass
                else:
                    # caso as chances da polícia esteja menor que 100%
                    print(f'\n{colors.red}+1%{colors.reset} de chance da polícia aparecer')
                    variables.chancePolicia = variables.chancePolicia + variables.aumentarChancePoliciaTrocaTiro
                input()
                break
            else:
                # morreu na troca de tiros
                print(f'\n{colors.red}Troca de tiros:{colors.reset} Você morreu na troca de tiros com a polícia. Fim de jogo.\n')
                exit()
        elif option == '3':
            # se entregar
            if variables.money < variables.fianca:
                # caso não tenha dinheiro
                print(f'\n{colors.red}Aviso:{colors.reset} Você não tem dinheiro para pagar a fiança. Você foi preso.')
                preso()
                input()
                break
            else:
                # caso tenha dinheiro
                print(f'\n{colors.red}Aviso:{colors.reset} Você se entregou, pagou a fiança e teve suas drogas apreendidas.')
                variables.drug = 0
                variables.money = variables.money - variables.fianca
                variables.fianca = variables.fianca + variables.aumentarFianca
                input()
                break
        else:
            # não escolher
            pass


def assaltar():
    # função para assaltar
    while True:
        title()

        print(f'{colors.blue}1.{colors.reset} Assaltar pessoas    [Chance: {colors.red}{variables.chanceAssaltarPessoas}%{colors.reset} | Máximo: {colors.yellow}R${variables.ganhosAssaltarPessoas}{colors.reset}]')
        print(f'\n{colors.blue}2.{colors.reset} Assaltar um banco   [Chance: {colors.red}{variables.chanceAssaltarBanco}%{colors.reset} | Máximo: {colors.yellow}R${variables.ganhosAssaltarBanco}{colors.reset}]')
        print(f'\n{colors.blue}0.{colors.reset} Voltar')
        opcao = str(input('\nOpção: '))

        title()

        if opcao == '1':
            # assaltar pessoas
            if random_number() <= variables.chanceAssaltarPessoas:
                # assalto bem-sucedido
                grana1 = gerar_dinheiro(variables.ganhosAssaltarPessoas)
                print(f'{colors.green}Aviso:{colors.reset} Você assaltou {colors.yellow}R${grana1}{colors.reset} de um pai de família.')
                variables.money = variables.money + grana1

                if variables.chanceAssaltarPessoas <= 1:
                    # não diminuir as chances caso seja 1 ou menor que 1
                    pass
                else:
                    # diminuir caso for maior que 1
                    print(f'\n{colors.red}-{variables.diminuirChancePessoas}%{colors.reset} de chance de assaltar pessoas.')
                    variables.chanceAssaltarPessoas = variables.chanceAssaltarPessoas - variables.diminuirChancePessoas

                input()
                break
            else:
                # assalto fracassado
                print(f'{colors.red}Aviso:{colors.reset} Você fracassou no assalto e foi preso em flagrante.')
                preso()

                input()
                break
        elif opcao == '2':
            # assaltar um banco
            if random_number() <= variables.chanceAssaltarBanco:
                # assalto bem-sucedido
                grana2 = gerar_dinheiro(variables.ganhosAssaltarBanco)
                print(f'{colors.green}Aviso:{colors.reset} Você assaltou {colors.yellow}R${grana2}{colors.reset} de um banco com sucesso.')
                variables.money = variables.money + grana2

                if variables.chanceAssaltarBanco <= 1:
                    # não zerar as chances de assaltar banco
                    pass
                else:
                    print(f'\n{colors.red}-{variables.diminuirChanceBanco}%{colors.reset} de chance de roubar bancos.')
                    variables.chanceAssaltarBanco = variables.chanceAssaltarBanco - variables.diminuirChanceBanco
                    
                print(f'\n{colors.red}+R${variables.aumentarFiancaBanco}{colors.reset} no preço da fiança')
                variables.fianca = variables.fianca + variables.aumentarFiancaBanco
                
                if variables.chancePolicia >= 100:
                    variables.chancePolicia = 100
                else:
                    print(f'\n{colors.red}+{variables.aumentarChancePolicia}%{colors.reset} de chance da polícia.')
                    variables.chancePolicia = variables.chancePolicia + variables.aumentarChancePolicia

                input()
                break
            else:
                # assalto fracassado
                print(f'{colors.red}Aviso:{colors.reset} Você fracassou no assalto a banco e foi preso em flagrante.')
                preso()

                input()
                break
        elif opcao == '0':
            # voltar
            break
        else:
            # nenhuma opcão válida digitada
            pass


def banco():
    # função do banco
    while True:
        if variables.contaAberta:
            # conta aberta
            title()

            print(f'Dinheiro: {colors.green}R${variables.money}{colors.reset}')

            if variables.saldoBloqueado:
                # saldo bloqueado
                print(f'\nSaldo Bancário: {colors.red}R${variables.saldoBanco}{colors.reset}')
            else:
                # saldo livre
                print(f'\nSaldo Bancário: {colors.green}R${variables.saldoBanco}{colors.reset}')

            if variables.devendoBanco <= 0:
                variables.emprestimoCheck = False

            if variables.emprestimoCheck == True:
                print(f'\nEmpréstimo: {colors.cyan}R${variables.devendoBanco} (R${variables.valorEmprestimo1} + {variables.juros}%){colors.reset}')

            print(f'\n{colors.blue}1.{colors.reset} Depositar')
            print(f'\n{colors.blue}2.{colors.reset} Sacar')

            if variables.emprestimoCheck == False:
                print(f'\n{colors.blue}3.{colors.reset} Empréstimo de R${variables.valorEmprestimo1} [Juros: {colors.red}{variables.juros}%{colors.reset}]')

            if variables.emprestimoCheck:
                print(f'\n{colors.blue}8.{colors.reset} Pagar todo o empréstimo')

            if variables.auxilioEmergencialCheck == False:
                print(f'\n{colors.blue}9.{colors.reset} Auxílio Emergencial de R${variables.auxilioEmergencial}')


            print(f'\n{colors.blue}0.{colors.reset} Voltar')
            option = str(input('\nOpção: '))

            if option == '1':
                # depositar
                if variables.saldoBloqueado == False:
                    # saldo não bloqueado
                    try:
                        deposito = int(input('\nDepositar: '))

                        if variables.money >= deposito:
                            # tem dinheiro para depositar
                            variables.saldoBanco = variables.saldoBanco + deposito
                            variables.money = variables.money - deposito
                            print(f'\n{colors.green}Banco:{colors.reset} Você depositou R${deposito} na sua conta.')
                            input()
                        else:
                            # sem dinheiro para depositar
                            print(f'\n{colors.red}Banco:{colors.reset} Você não tem R${deposito} para depositar.')
                            input()
                    except:
                        pass
                else:
                    # saldo bloqueado
                    print(f'\n{colors.red}Banco:{colors.reset} Seu saldo foi bloqueado devido a muitas prisões.')
                    input()
            elif option == '2':
                # sacar
                if variables.saldoBloqueado == False:
                    # saldo não bloqueado
                    try:
                        sacar = int(input('\nSacar: '))

                        if variables.saldoBanco >= sacar:
                            # tem saldo suficiente
                            variables.money = variables.money + sacar
                            variables.saldoBanco = variables.saldoBanco - sacar
                            print(f'\n{colors.green}Banco:{colors.reset} Você sacou R${sacar} da sua conta bancária.')
                            input()
                        else:
                            # não tem saldo suficiente
                            print(f'\n{colors.red}Banco:{colors.reset} Você não tem R${sacar} para sacar.')
                            input()
                    except:
                        pass
                else:
                    # saldo bloqueado
                    print(f'\n{colors.red}Banco:{colors.reset} Seu saldo está bloqueado devido a muitas prisões.')
                    input()
            elif option == '3':
                # empréstimo bancário
                if variables.emprestimoCheck:
                    # já tem um empréstimo
                    print(f'\n{colors.red}Empréstimo:{colors.reset} Você já tem uma dívida em aberto.')
                    input()
                else:
                    # ainda não tem empréstimo
                    if variables.foiPreso:
                        # já foi preso
                        print(f'\n{colors.red}Empréstimo:{colors.reset} Não é feito empréstimos para ex-presidiários.')
                        input()
                    else:
                        # nunca foi preso
                        print(f'\n{colors.green}Empréstimo:{colors.reset} Você obteve um empréstimo de R${variables.valorEmprestimo1} com {variables.juros}% de juros.')
                        variables.emprestimoCheck = True
                        variables.money = variables.money + variables.valorEmprestimo1
                        variables.devendoBanco = variables.devendoBanco + (variables.valorEmprestimo1 + variables.valorJuros)
                        input()
            elif option == '8':
                # pagar todo o empréstimo
                if variables.emprestimoCheck:
                    # está devendo o banco
                    if variables.money >= variables.devendoBanco:
                        # tem dinheiro para pagar o empréstimo
                        print(f'\n{colors.green}Empréstimo:{colors.reset} Você pagou R${variables.devendoBanco} que estava devendo ao banco.')
                        variables.money = variables.money - variables.devendoBanco
                        variables.emprestimoCheck = False
                        variables.devendoBanco = 0
                        input()
                    else:
                        # sem dinheiro para pagar o empréstimo
                        print(f'\n{colors.red}Empréstimo:{colors.reset} Você não tem R${variables.devendoBanco} para pagar o banco.')
                        input()
                else:
                    # não está devendo o banco
                    pass
            elif option == '9':
                # obter o auxílio emergencial
                if variables.auxilioEmergencialCheck == False:
                    # caso ainda não pegou o auxílio
                    if variables.foiPreso:
                        # caso já tenha sido preso
                        print(f'\n{colors.red}Auxílio Emergencial:{colors.reset} Auxílio negado para ex-presidiários.')
                        variables.auxilioEmergencialCheck = True
                        input()
                    else:
                        # caso não tenha sido preso
                        print(f'\n{colors.green}Auxílio Emergencial:{colors.reset} Você obteve R${variables.auxilioEmergencial} do auxílio emergencial.')
                        variables.money = variables.money + variables.auxilioEmergencial
                        variables.auxilioEmergencialCheck = True
                        input()
                else:
                    # caso já tenha pegado o auxílio
                    pass
            elif option == '0':
                # voltar
                break
        else:
            # a conta ainda não foi aberta
            title()

            print(f'{colors.red}Aviso:{colors.reset} Não poderá abrir uma conta tendo menos de R${variables.minimoAbrirConta} ou se já foi preso.')
            
            if variables.foiPreso:
                # caso tenha sido preso
                print(f'\n{colors.red}1. Abrir uma conta{colors.reset} ')
            else:
                # caso não tenha sido preso
                print(f'\n{colors.blue}1.{colors.reset} Abrir uma conta')

            print(f'\n{colors.blue}0.{colors.reset} Voltar')

            opcao = str(input(f'\nOpção[{colors.blue}R${variables.money}{colors.reset}]: '))

            if opcao == '1':
                # abrir conta
                if variables.money >= variables.minimoAbrirConta and variables.foiPreso == False:
                    # conta aberta com sucesso
                    variables.contaAberta = True
                    print(f'\n{colors.green}Banco:{colors.reset} A conta no banco foi aberta com sucesso!')
                    input()
                elif variables.foiPreso == True:
                    # já foi preso e não poderá abrir a conta
                    print(f'\n{colors.red}Banco:{colors.reset} Você já foi preso e nunca poderá abrir uma conta.')
                    input()
                elif variables.money < variables.minimoAbrirConta:
                    # sem dinheiro para abrir a conta
                    print(f'\n{colors.red}Banco:{colors.reset} Sem dinheiro para abrir uma conta.')
                    input()
            elif opcao == '0':
                # voltar
                break
            else:
                # nenhuma opção selecionada
                pass


def save():
    # função para salvar o jogo
    fileName = variables.playerName + '.txt'
    dados = [str(variables.playerName),
             str(variables.drugName),
             int(variables.drug),
             int(variables.money),
             bool(variables.foiPreso),
             int(variables.vezesPreso)]

    while True:
        if path.exists(fileName):
            # o arquivo já existe
            remove(fileName)
        else:
            # o arquivo não existe, mas foi criado
            with open(fileName, 'w+') as create_file:
                create_file.close()
                break
    with open(fileName, 'w') as write_file:
        for i in range(0, len(dados)):
            write_file.writelines(dados[i])
        write_file.close()


def obter_dados():
    # obter todos os dados do save
    pass


def upgrades():
    # função para fazer upgrades
    while True:
        title()

        print(f'{colors.green}Lista de upgrades{colors.reset}')

        if variables.diminuirTempoProducaoCheck == False:
            # ainda não comprou esse item
            print(f'\n{colors.blue}1.{colors.reset} Diminuir {variables.diminuirTempoProducao} segundo da produção de drogas [Preço: {colors.yellow}R${variables.diminuirTempoProducaoPreco}{colors.reset}]')
        else:
            # já comprou esse item
            print(f'\n{colors.blue}1.{colors.reset} Diminuir {variables.diminuirTempoProducao} segundo da produção de drogas [Preço: {colors.red}COMPRADO{colors.reset}]')

        if variables.aumentarMultiplicadorDeGanhosCheck == False:
            # ainda não comprou esse item
            print(f'\n{colors.blue}2.{colors.reset} Duplicar ganhos na venda de drogas [Preço: {colors.yellow}R${variables.aumentarMultiplicadorDeGanhosPreco}{colors.reset}]')
        else:
            # já comprou esse item
            print(f'\n{colors.blue}2.{colors.reset} Duplicar ganhos na venda de drogas [Preço: {colors.red}COMPRADO{colors.reset}]')

        if variables.diminuirChanceCorrerDaPoliciaCheck == False:
            # ainda não comprou esse item
            print(f'\n{colors.blue}3.{colors.reset} Aumentar 30% de chance de correr da polícia [Preço: {colors.yellow}R${variables.diminuirChanceCorrerDaPoliciaPreco}{colors.reset}]')
        else:
            # já comprou esse item
            print(f'\n{colors.blue}3.{colors.reset} Aumentar 30% de chance de correr da polícia [Preço: {colors.red}COMPRADO{colors.reset}]')

        print(f'\n{colors.blue}4.{colors.reset} Limpar ficha de prisão [Preço: {colors.yellow}R${variables.limparPrisoesPreco}{colors.reset} | Próximo preço: R${variables.limparPrisoesPreco + variables.aumentarLimparPrisoes}]')

        print(f'\n{colors.blue}0.{colors.reset} Voltar')

        opcao = str(input(f'\nOpção[{colors.blue}R${variables.money}{colors.reset}]: '))

        if opcao == '1':
            # menos 1 segundo para produzir drogas
            if variables.diminuirTempoProducaoCheck == False:
                # ainda não comprou
                if variables.money >= variables.diminuirTempoProducaoPreco:
                    # tem dinheiro
                    variables.money = variables.money - variables.diminuirTempoProducaoPreco
                    variables.tempoProduzirDrogas = variables.tempoProduzirDrogas - variables.diminuirTempoProducao
                    variables.diminuirTempoProducaoCheck = True
                else:
                    # sem dinheiro
                    avisos(1)
            else:
                # já comprou
                avisos(0)
        elif opcao == '2':
            # dublicar ganhos na venda de drogas
            if variables.aumentarMultiplicadorDeGanhosCheck == False:
                # ainda não comprou
                if variables.money >= variables.aumentarMultiplicadorDeGanhosPreco:
                    # tem dinheiro
                    variables.money = variables.money - variables.aumentarMultiplicadorDeGanhosPreco
                    variables.multiplicador = variables.multiplicador + variables.aumentarMultiplicadorDeGanhos
                    variables.aumentarMultiplicadorDeGanhosCheck = True
                else:
                    # sem dinheiro
                    avisos(1)
            else:
                # já comprou
                avisos(0)
        elif opcao == '3':
            # diminuir chances de correr na polícia
            if variables.diminuirChanceCorrerDaPoliciaCheck == False:
                # ainda não comprou
                if variables.money >= variables.diminuirChanceCorrerDaPoliciaPreco:
                    # tem dinheiro
                    variables.money = variables.money - variables.diminuirChanceCorrerDaPoliciaPreco
                    variables.chanceCorrer = variables.chanceCorrer + variables.diminuirChanceCorrerDaPolicia
                    variables.diminuirChanceCorrerDaPoliciaCheck = True
                else:
                    # sem dinheiro
                    avisos(1)
            else:
                # já comprou
                avisos(0)
        elif opcao == '4':
            # limpar ficha de prisão
            if variables.foiPreso:
                # caso já foi preso
                if variables.money >= variables.limparPrisoesPreco:
                    # tem dinheiro
                    variables.money = variables.money - variables.limparPrisoesPreco
                    variables.foiPreso = False
                    variables.vezesPreso = 0
                    variables.limparPrisoesPreco = variables.limparPrisoesPreco + variables.aumentarLimparPrisoes
                else:
                    # não tem dinheiro
                    avisos(1)
            else:
            # caso ainda não foi preso
                avisos(2)
        elif opcao == '0':
            # voltar
            break
        else:
            pass


def avisos(numero):
    # frases/avisos para evitar repetição

    if numero == 0:
        # avisar que já comprou o item
        print(f'\n{colors.red}Upgrade:{colors.reset} Você já comprou esse item.')
    elif numero == 1:
        # avisar que não tem dinheiro para comprar o item
         print(f'\n{colors.red}Upgrade:{colors.reset} Sem dinheiro para comprar esse item.')
    elif numero == 2:
        # avisar que ainda não foi preso para comprar o item
        print(f'\n{colors.red}Prisão:{colors.reset} Você não foi preso para poder comprar esse item.')
    input()


def importar_drogas():
    # função para importar drogas
    while True:
        title()

        print('Importação de Drogas')
        print(f'\n{colors.blue}1.{colors.reset} Importar {colors.cyan}{variables.importar1Gramas}g{colors.reset}     [Preço: {colors.yellow}R${variables.importar1Preco}{colors.reset} | Chance: {colors.red}{variables.importar1Chance}%{colors.reset}]')
        print(f'\n{colors.blue}2.{colors.reset} Importar {colors.cyan}{variables.importar2Gramas}g{colors.reset}     [Preço: {colors.yellow}R${variables.importar2Preco}{colors.reset} | Chance: {colors.red}{variables.importar2Chance}%{colors.reset}]')
        print(f'\n{colors.blue}3.{colors.reset} Importar {colors.cyan}{variables.importar3Gramas}g{colors.reset}     [Preço: {colors.yellow}R${variables.importar3Preco}{colors.reset} | Chance: {colors.red}{variables.importar3Chance}%{colors.reset}]')
        print(f'\n{colors.blue}4.{colors.reset} Importar {colors.cyan}{variables.importar4Gramas}g{colors.reset}    [Preço: {colors.yellow}R${variables.importar4Preco}{colors.reset} | Chance: {colors.red}{variables.importar4Chance}%{colors.reset}]')
        print(f'\n{colors.blue}5.{colors.reset} Importar {colors.cyan}{variables.importar5Gramas}g{colors.reset}    [Preço: {colors.yellow}R${variables.importar5Preco}{colors.reset} | Chance: {colors.red}{variables.importar5Chance}%{colors.reset}]')
        print(f'\n{colors.blue}6.{colors.reset} Importar {colors.cyan}{variables.importar6Gramas}g{colors.reset}    [Preço: {colors.yellow}R${variables.importar6Preco}{colors.reset} | Chance: {colors.red}{variables.importar6Chance}%{colors.reset}]')
        print(f'\n{colors.blue}0.{colors.reset} Voltar')

        option = str(input(f'\nOpção[{colors.blue}R${variables.money}{colors.reset}]: '))

        if option == '0':
            # voltar
            break
        elif option == '1':
            # importar 1
            importacao_resultado(variables.importar1Gramas, variables.importar1Preco, variables.importar1Chance)
        elif option == '2':
            # importar 2
            importacao_resultado(variables.importar2Gramas, variables.importar2Preco, variables.importar2Chance)
        elif option == '3':
            # importar 3
            importacao_resultado(variables.importar3Gramas, variables.importar3Preco, variables.importar3Chance)
        elif option == '4':
            # importar 4
            importacao_resultado(variables.importar4Gramas, variables.importar4Preco, variables.importar4Chance)
        elif option == '5':
            # importar 5
            importacao_resultado(variables.importar5Gramas, variables.importar5Preco, variables.importar5Chance)
        elif option == '6':
            # importar 6
            importacao_resultado(variables.importar6Gramas, variables.importar6Preco, variables.importar6Chance)


def importacao_resultado(gramas, preco, chance):
    # resultados da importação de drogas
    if variables.money >= preco:
        # tem dinheiro para a importar
        for second in reversed(range(1, variables.tempoImportar + 1)):
            title()
            print(f'Tentando importar {gramas}g de {variables.drugName} em {colors.yellow}{second}{colors.reset} segundos...')
            sleep(1)
        
        title()

        if random_number() <= chance:
            # importação bem-sucedida
            print(f'\n{colors.green}Importação:{colors.reset} Sua importação passou pelas fronteiras sem problemas.')
            print(f'\nGanhou: {colors.yellow}{gramas}g{colors.reset} | Preço: {colors.red}-R${preco}{colors.reset}')
            
            variables.money = variables.money - preco
            variables.drug = variables.drug + gramas
        else:
            # importação fracassada
            print(f'\n{colors.red}Importação:{colors.reset} A polícia apreendeu suas drogas importadas.')
            print(f'\nPerdeu: {colors.red}-R${preco}{colors.reset}')
            
            variables.money = variables.money - preco
    else:
        # sem dinheiro para importar
        print(f'\n{colors.red}Importação:{colors.reset} Sem dinheiro para importar {gramas}g de {variables.drugName}.')
    input()


def emprestimo(valor, vendido):
    # função para tratar os empréstimos
    dividir = 0
    banco = 0
    receber = 0

    if valor % 2 == 0:
        # par
        dividir = int(valor / 2)
        receber = dividir
        banco = dividir

        if dividir >= variables.devendoBanco:
            # ganho maior que a dívida
            quitar = dividir - variables.devendoBanco
            banco = banco - quitar
            receber = receber + quitar

            variables.money = variables.money + receber
            variables.devendoBanco = variables.devendoBanco - banco
        else:
            variables.money = variables.money + receber
            variables.devendoBanco = variables.devendoBanco - banco
    else:
        # ímpar
        exit()

    variables.drug = variables.drug - vendido
    print(f'\nVendeu: {colors.yellow}{vendido}g{colors.reset} | Ganhos: {colors.green}R${receber}{colors.reset} | Banco: {colors.cyan}R${banco}{colors.reset}')

    if variables.devendoBanco <= 0 and variables.emprestimoCheck:
        # quitou as dívidas do banco
        print(f'\n{colors.green}Empréstimo:{colors.reset} Você quitou sua dívida de R${variables.valorEmprestimo1 + variables.valorJuros} do banco.')
    

def nome_droga():
    # retorna um nome de droga aleatório
    names = ['Cocaína',
             'Crack',
             'Maconha',
             'Ecstasy',
             'LSD',
             'Morfina',
             'Heroína',
             'Clorofórmio',
             'Ópio',
             'Cogumelo',
             'Álcool',
             'Tabaco',
             'Haxixe',
             'Quetamina',
             'Cigarro',
             'Pão',
             'Mortadela',
             'Crianças',
             'Orgãos',
             'Humanos',
             'Lobisomens',
             'Corpos',
             'Mulheres',
             'Homens',
             'Porcarias',
             'Doces',
             'Asiáticas',
             'Pastel',
             'Balinhas',
             'Travestis',
             'Leonans']
    return choice(names)


def frases_drogas(quantidade, preco):
    # retorna frases e nome dos clientes
    clientes = [f'E ai caraí, manda {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}.',
                f'Fala maninho, quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, manda aí.',
                f'Fala ai fi da peste, tô afim de {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}.',
                f'Opa, e ai corno, manda {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pro pai aqui.',
                f'Vai logo tio, quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pra ontem.',
                f'Vai gay do caralho, manda logo meus {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}.',
                f'Salve mano, hoje vou querer {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}.',
                f'Tô muito doidão caralho, manda logo {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} aí porra.',
                f'Porra caralho, tô afim de {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, a sua é muito boa.',
                f'PORRRAAAA! {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pra agoraaaaaa.',
                f'Salve quebrada, tô sabendo que tu tem {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, manda aí.',
                f'Foda-se minha vida, quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pra ver se morro logo nessa porra.',
                f'Ala o boiola vendendo {variables.drugName}, manda {colors.yellow}{quantidade}g{colors.reset} ai porra.',
                f'Vai, manda {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, cuidado com a polícia parceiro.',
                f'Minha mãe quer {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, da ai tio.',
                f'Oii gostoso(a), quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, vem na minha casa depois.',
                f'Vai te fuder, VAI TE FUDERRRRRR.... {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} agora agora agoraaaa.',
                f'Odeio drogas, porém quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} para ver como é.',
                f'Meu médico receitou {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName}, preciso pra agora.',
                f'Tu é o melhor vendedor do pedaço, manda {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} ai amigão.',
                f'Quero {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pra enfiar no meu cu.',
                f'Se {variables.drugName} mata, então eu quero {colors.yellow}{quantidade}g{colors.reset}.',
                f'Sou a decepção da minha família, manda {colors.yellow}{quantidade}g{colors.reset} de {variables.drugName} pra ver se morro logo.']

    nomes = ['Victor', 'Carlos', 'Layon', 'Luan', 'Leonan', 'Jhennyfer', 'Cláudia', 'Liliane', 'Dona Lina',
             'Leandro', 'Bolsonaro', 'Lula', 'Dilma']

    return [choice(nomes), choice(clientes)]