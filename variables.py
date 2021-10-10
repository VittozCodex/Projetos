# jogador
playerName = ''  # nome do jogador
drugName = ''  # nome da droga
drug = 100  # quantidade de drogas atual/inicial
money = 500  # quantidade de dinheiro atual/inicial
foiPreso = False  # verifica se foi preso ou não
vezesPreso = 0  # quantidade de vezes que foi preso

# produção de drogas
#nivelProducao = 1  # nível correspondente a produção de drogas
gramas = 10  # valor da produção de droga
tempoProduzirDrogas = 3  # tempo para a produção da droga
aumentarGramas = 10  # quantidade que irá aumentar a cada melhoria da produção
aumentarDepois100 = 20  # aumentar a quantidade de drogas quando a produção for maior que 100
precoProducao = 500  # preço da melhoria atual/inicial
aumentarPrecoMelhoria = 500  # quantidade que irá aumentar do preço da melhoria

# vender drogas
nomeCliente = 'Cliente'  # nome dos clientes que comprará as drogas
chancePolicia = 5  # chance em porcentagem da polícia aparecer
chanceCorrer = 50  # chance de conseguir fugir da polícia correndo
chanceTrocarTiro = 70  # chance de ter sucesso ao trocar tiro com a polícia
aumentarChancePoliciaTrocaTiro = 1  # aumenta cada vez que você mata um policial
fianca = 100  # preço da fiança atual/inicial
aumentarFianca = 500  # quantidade que irá aumentar de fiança a cada vez que pagar
multiplicador = 2  # a quantidade de droga vendida será multiplicado por este valor e trocará em dinheiro

# assaltar
chanceAssaltarPessoas = 60  # chance de assaltar pessoas
ganhosAssaltarPessoas = 1500  # máximo de dinheiro que pode roubar das pessoas
diminuirChancePessoas = 2  # irá diminuir a porcentagem a cada vez que o assalto der certo

chanceAssaltarBanco = 30  # chance de assaltar um banco
ganhosAssaltarBanco = 100000  # máximo de dinheiro que pode roubar do banco
diminuirChanceBanco = 10  # irá diminuir a cada vez que o assalto der certo
aumentarChancePolicia = 15  # irá aumentar a chance da polícia quando assaltar um banco
aumentarFiancaBanco = 2000  # irá aumentar o preço da fiança

maximoVezesPreso = 5  # quantidade máxima que poderá ser preso
bloquearConta = 2  # quantidade máxima que pode ser preso antes de bloquear a conta do banco

# banco
contaAberta = False  # verifica se a conta do banco foi aberta ou não
minimoAbrirConta = 1000  # mínimo de dinheiro para abrir uma conta
saldoBanco = 0  # saldo armazenado no banco
saldoBloqueado = False  # verifica se o saldo no banco está bloqueado

auxilioEmergencial = 600  # valor do auxílio emergencial
auxilioEmergencialCheck = False  # verifica se já pegou o auxílio

valorEmprestimo1 = 3000 # valor do empréstimo 1
devendoBanco = 0  # quantos está devendo ao banco
emprestimoCheck = False  # verifica se está devendo o banco
juros = 20  # porcentagem de juros
valorJuros = int((valorEmprestimo1 * juros) / 100)

# upgrades
diminuirTempoProducao = 1  # quantidade que irá diminuir no tempo da produção de drogas
diminuirTempoProducaoCheck = False # Checar se a compra já foi feita
diminuirTempoProducaoPreco = 500 # preço da melhoria

aumentarMultiplicadorDeGanhos = 2  # aumentar o quanto vai multiplicar os ganhos
aumentarMultiplicadorDeGanhosCheck = False  # checar se a compra já foi feita
aumentarMultiplicadorDeGanhosPreco = 1000  # preço da melhoria

diminuirChanceCorrerDaPolicia = 30  # porcentagem que irá aumentar do upgrade
diminuirChanceCorrerDaPoliciaCheck = False  # checar se a compra já foi feita
diminuirChanceCorrerDaPoliciaPreco = 1500  # preço da melhoria

limparPrisoesCheck = False  # checar se a compra já foi feita
limparPrisoesPreco = 1500  # preço para limpar as prisões
aumentarLimparPrisoes = 8500  # preço que irá aumentar a cada compra

# importar drogas
tempoImportar = 3  # tempo para finalizar a importação

importar1Gramas = 100  # gramas importar 1
importar1Preco = 50  # preco importar 1
importar1Chance = 60  # chance importar 1

importar2Gramas = 300  # gramas importar 2
importar2Preco = 150  # preco importar 2
importar2Chance = 50  # chance importar 2

importar3Gramas = 500  # gramas importar 3
importar3Preco = 300  # preco importar 3
importar3Chance = 40  # chance importar 3

importar4Gramas = 1000  # gramas importar 4
importar4Preco = 500  # preco importar 4
importar4Chance = 30  # chance importar 4

importar5Gramas = 3000  # gramas importar 5
importar5Preco = 1500  # preco importar 5
importar5Chance = 20  # chance importar 5

importar6Gramas = 5000  # gramas importar 6
importar6Preco = 3000  # preco importar 6
importar6Chance = 10  # chance importar 6