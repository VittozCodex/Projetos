# bibliotecas personalizadas
import colors
import variables
import extras
# bibliotecas python
from time import sleep

# variáveis
cor = colors

def get_infos():
    # obter as informações iniciais do jogador
    checarNomes = False
    while checarNomes != True:
        extras.title()
        variables.playerName = input(f'{cor.cyan}•{cor.reset} Nome do traficante:{cor.yellow} ')
        variables.drugName = input(f'\n{cor.reset}{cor.cyan}•{cor.reset} Nome da droga (opcional): ')
        checarNomes = extras.verificar_nomes(variables.playerName, variables.drugName)

    print(f'\n{cor.yellow}{variables.playerName}{cor.reset}, o(a) vendedor(a) de {cor.yellow}{variables.drugName}{cor.reset}.')
    print(f'{cor.green}\nPressione ENTER para começar...{cor.reset}')
    input()


def produzir_droga():
    # função para produzir drogas
    tempo = variables.tempoProduzirDrogas

    for seconds in reversed(range(1, tempo + 1)):
        extras.title()

        if variables.diminuirTempoProducaoCheck:
            print(f'{colors.magenta}[UPGRADE]{colors.reset}\n')

        print(f'Produzindo {variables.gramas}g de {variables.drugName} em {cor.yellow}{seconds}{cor.reset} segundos.')
        sleep(1)
    variables.drug = variables.drug + variables.gramas


def melhorar_producao():
    # função para melhorar a produção de drogas
    if variables.money >= variables.precoProducao:
        #variables.nivelProducao = variables.nivelProducao + 1

        if variables.gramas >= 100:
            variables.gramas = variables.gramas + variables.aumentarDepois100
        else:
            variables.gramas = variables.gramas + variables.aumentarGramas

        variables.money = variables.money - variables.precoProducao
        variables.precoProducao = variables.precoProducao + variables.aumentarPrecoMelhoria
    else:
        print(f'\nFaltam {cor.yellow}R${variables.precoProducao - variables.money}{cor.reset} para melhorar a produção de drogas.')
        input()


def vender_drogas():
    # função para vender as drogas
    extras.title()

    quantidade = extras.gerar_drogas(variables.drug)
    preco = quantidade * variables.multiplicador

    nome, frase = extras.frases_drogas(quantidade, preco)

    print(f'Vendendo drogas... [Polícia: {cor.red}{variables.chancePolicia}%{cor.reset}]')

    if variables.aumentarMultiplicadorDeGanhosCheck:
        # caso o upgrade foi comprado
        print(f'\n{colors.magenta}[UPGRADE]{colors.reset}')

    print(f'\n• {nome}: {frase}')
    sleep(0.5)
    print(f'\n• {variables.playerName}: Beleza, vai ficar por {colors.green}R${preco}{colors.reset}.')
    sleep(1)

    if variables.emprestimoCheck == False:
        # não tem dívidas com o banco
        variables.drug = variables.drug - quantidade
        variables.money = variables.money + preco

        print(f'\nVendeu: {cor.yellow}{quantidade}g{cor.reset} | Ganhou: {colors.green}R${preco}{colors.reset}')    
        input()
    else:
        # tem dívidas com o banco
        extras.emprestimo(preco, quantidade)
        input()

    if extras.random_number() <= variables.chancePolicia:
        # verificar se a polícia vai aparecer
        extras.policia_drogas()


def menu():
    # menu principal do jogo

    while True:
        extras.verificar()
        extras.title()

        print(f'Traficante:   {cor.yellow}{variables.playerName.strip()}{cor.reset}')
        print(f'Droga:        {cor.yellow}{variables.drugName.strip()}{cor.reset}')
        print(f'Quantidade:   {cor.yellow}{variables.drug}g{cor.reset}')
        print(f'Dinheiro:     {cor.yellow}R${variables.money}{cor.reset}')
        
        if variables.contaAberta:
            # verificar se a conta do banco foi aberta
            if variables.saldoBloqueado:
                # caso o saldo estiver bloqueado
                if variables.emprestimoCheck:
                    # devendo o banco
                    print(f'Banco:        {cor.red}Bloqueado{cor.reset} - {cor.cyan}R${variables.devendoBanco}{cor.reset}')
                else:
                    # não está devendo o banco
                    print(f'Banco:        {cor.red}Bloqueado{cor.reset}')
            else:
                # caso o saldo não estiver bloqueado
                if variables.emprestimoCheck:
                    # devendo o banco
                    print(f'Banco:        {cor.yellow}R${variables.saldoBanco}{cor.reset} - {cor.cyan}R${variables.devendoBanco}{cor.reset}')
                else:
                    # não está devendo o banco
                    print(f'Banco:        {cor.yellow}R${variables.saldoBanco}{cor.reset}')
        if variables.foiPreso:
            # caso já foi preso
            print(f'Preso:        {cor.red}{variables.vezesPreso}/{variables.maximoVezesPreso} vez(es){cor.reset}')
        if extras.cheatAtivo:
            # caso usou cheat
            print(f'Cheat:        {cor.red}Ativado{cor.reset}')

        print(f'\n{cor.blue}1.{cor.reset} Produzir +{variables.gramas}g de {variables.drugName}')
        print(f'\n{cor.blue}2.{cor.reset} Vender drogas')
        print(f'\n{cor.blue}3.{cor.reset} Melhorar produção [Preço: R${variables.precoProducao}]')
        print(f'\n{cor.blue}4.{cor.reset} Assaltar')
        print(f'\n{cor.blue}5.{cor.reset} Banco')
        print(f'\n{cor.blue}6.{cor.reset} Upgrades')
        print(f'\n{cor.blue}7.{cor.reset} Importar drogas')

        opcao = str(input(f'\n{cor.green}•{cor.reset} Opção (/help): '))


        if '/' in opcao:
            # trapaças
            extras.cheats(opcao.split())
        elif opcao == '1':
            # produzir drogas
            produzir_droga()
        elif opcao == '2':
            # vender drogas
            if variables.drug < 1:
                print(f'\n{cor.red}Aviso:{cor.reset} Sem drogas para vender.')
                input()
            else:
                vender_drogas()
        elif opcao == '3':
            # melhorar a produção de drogas
            melhorar_producao()
        elif opcao == '4':
            # assaltar
            extras.assaltar()
        elif opcao == '5':
            # banco
            extras.banco()
        elif opcao == '6':
            # upgrades
            extras.upgrades()
        elif opcao == '7':
            # importar drogas
            extras.importar_drogas()


# início do programa
if __name__ == '__main__':
    get_infos()
    menu()
 