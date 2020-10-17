import os
from datetime import datetime, timezone, timedelta

# Strings para data e hora de SP feito com o auxilio da página: http://blog.alura.com.br/lidando-com-datas-e-horarios-no-python/
#Declara o fuso horário
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)
#Pega data e hora atual
data_e_hora_atuais = datetime.now()
#Pega data e hora atual de acordo com o fuso de SP
data_e_hora_atuais = data_e_hora_atuais.astimezone(fuso_horario)
#Faz a formatação de hora
data_e_hora_atuais = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#Declaração da lista dados, que dentro das funções vai conter as linhas do arquivo
dados = []

#Código de validação de CPF retirado do link https://code.sololearn.com/cZ20I1rin3Ks/#py Todos os direitos reservados ao desenvolvedor do algoritmo.
#Pedro Maimere, perfil: https://www.sololearn.com/Profile/7222761
def cpf_valido(cpf):
    mult1 = (10,9,8,7,6,5,4,3,2)
    dv1 = 0
    for n in range(9):
        dv1 += mult1[n]*int(cpf[n])
    if dv1 % 11 < 2:
        dv1 = '0'
    else:
        dv1 = str(11 - (dv1 % 11))
    cpf1 = cpf[:-2] + dv1
    mult2 = (11,10,9,8,7,6,5,4,3,2)
    dv2 = 0
    for n in range(10):
        dv2 += mult2[n]*int(cpf1[n])
    if dv2 % 11 < 2:
        dv2 = '0'
    else:
        dv2 = str(11 - (dv2 % 11))
    if cpf == cpf1 + dv2:
        return True
    else:
        return False

#Função para criar cliente
def criaCliente():
    #Tarifa inicial
    tarifa = 0
    #Input do nome do usuário
    nome = input("Digite seu nome: ")
    while True:
        #Input e validação do cpf de acordo com as cláusulas
        cpf = input("Digite seu CPF, sem '.' e '-': ")
        #Verifica se o cpf contém apenas números, tamanho do cpf e se o mesmo é válido de acordo com a função cpf_valido
        if cpf.isdecimal() and len(cpf) == 11 and cpf_valido(cpf):
            break;
        elif cpf.isdecimal() == False and len(cpf) != 11:
            print("Digite apenas números e um cpf de 11 dígitos.\n")
        elif not (len(cpf) == 11):
            print("O cpf não contém exatamente 11 dígitos.\n")
        elif not (cpf.isdecimal()):
            print("O cpf só pode conter dígitos NUMÉRICOS.\n")
        elif not (cpf_valido(cpf)):
            print("CPF inválido.\n")

    while True:
        #Informa detalhes sobre os tipo de contas dísponíveis no banco
        print("Escolha o conta que mais combina com o que o(a) sr(a) necessita.")
        print("Opção 1 - Conta Salário")
        print("     *Cobra taxa de 5% a cada débito realizado")
        print("     *Não permite débitos que deixem a conta com saldo negativo\n")
        print("Opção 2 - Conta Comum")
        print("     *Cobra taxa de 3% a cada débito realizado")
        print("     *Permite um saldo negativo de até (R$ 500,00)\n")
        print("Opção 3 - Conta Plus")
        print("     *Cobra taxa de 1% a cada débito realizado")
        print("     *Permite um saldo negativo de até (R$ 5.000,00)\n")
        #Input do tipo de conta
        tipoConta = input("Digite o número de opção que deseja: ")
        #Verifica a opção escolhida e aplica o tipo da conta a variável tipoConta
        if tipoConta == "1":
            print("Tipo de conta escolhido: Salário.\n")
            nomeConta = "Salario"
            break
        elif tipoConta == "2":
            print("Tipo de conta escolhido: Comum.\n")
            nomeConta = "Comum"
            break
        elif tipoConta == "3":
            print("Tipo de conta escolhido: Plus.\n")
            nomeConta = "Plus"
            break
        else:
            print("Opção inválida.\n")
    while True:
        #Input do valor inicial da conta
        valInicial = float(input("Digite o valor inicial da sua conta: "))
        #Verifica se o valor inicial é positivo
        if valInicial >= 0:
            break
        else:
            print("Valor inválido, não são permitidos valores negativos.\n")
    while True:
        #Input da senha
        senha = input("Digite uma senha de 8 dígitos numéricos: ")
        #Verifica o tamanho da senha, e se ela contém apenas números
        if len(senha) == 8 and senha.isdecimal():
            #Confirmação de senha
            confirmSenha = input("Confirme sua senha: ")
            #Verifica se a senha é igual a confirmação
            if senha == confirmSenha:
                print("Conta criada com sucesso.\n")
                break
            else:
                print("As senhas digitadas não coincidem.\n")
        #Cláusulas que verificam o tamanho da senha, e se ela contém apenas números para informar os devidos erros
        elif len(senha) != 8 and senha.isdecimal():
            if len(senha) > 8:
                print("A senha possui mais que 8 dígitos.\n")
            elif len(senha) < 8:
                print("A senha possui menos que 8 dígitos.\n")
        elif len(senha) == 8 and senha.isdecimal() == False:
            print("A senha só deve conter dígitos NUMÉRICOS.\n")
    #Abre o arquivo do usuário com nome "cpf.txt"
    arquivo = open(cpf + ".txt", "w")
    #Escreve o nome,cpf,tipo de conta, e a primeira transação, no caso o valor inicial, com data e hora de execução.
    arquivo.write("Nome: " + nome + "\n")
    arquivo.write("CPF: " + cpf + "\n")
    arquivo.write("Conta: " + nomeConta + "\n")
    arquivo.write("Data: %s   +   %15.2f                       Tarifa:       %15.2f                    Saldo:     %15.2f\n" %
        (data_e_hora_atuais, valInicial, tarifa, valInicial))
    #Fechamento do arquivo principal
    arquivo.close()

    #Abre o arquivo com login do usuário(cpf e senha)
    arq_senha = open("login_" + cpf + ".txt", "w")
    #Escreve cpf e senha no arquivo
    arq_senha.write(cpf + "\n")
    arq_senha.write(senha + "\n")
    #Fechamento do arquivo de senha
    arq_senha.close()


#Função para apagar cliente
def apagaCliente():
    #Pega o cpf do cliente a ser deletado.
    cpf = input("Digite o CPF: ")
    #Remove o arquivo do sistema.
    os.remove(cpf + ".txt")
    os.remove("login_" + cpf + ".txt")
    print("Cliente removido com sucesso.\n")

#Função de Débito
def debitaConta():
    dados = []
    #Pega o cpf do cliente
    cpf = input("Digite o CPF: ")
    #Pega a senha
    senha_digitada = input("Digite sua senha: ")
    #Abre o arquivo de senha do respectivo cpf e pega a senha que está guardada no arquivo
    arq_senha = open("login_" + cpf + ".txt")
    linha_arq_senha = arq_senha.readlines()
    senha = linha_arq_senha[1]
    #Fecha o arquivo de senha
    arq_senha.close()
    #Compara a senha digitada com a do arquivo
    if senha_digitada == senha.strip():
        while True:
            # Pega o valor do débito
            debito = float(input("Digite o valor a ser debitado: "))
            # Verifica se é maior que 0
            if debito > 0:
                break
            elif debito < 0:
                print("Debite entrando com um valor positivo.\n")
            else:
                print("Debite um valor maior que 0.\n")
        #Abre o arquivo do usuario pelo cpf e lê todas as linhas do mesmo
        arquivo = open(cpf + ".txt", "r")
        for linha in arquivo.readlines():
            #Separa as linhas e passa passa para a list dados
            linha_sep = linha.split(" ")
            dados.append(linha_sep)

        #Pega o tipo de conta do usuário
        tipoConta = dados[2][1].strip()
        #Verifica a tarifa e o saldo mínimo de acordo com o tipo de conta
        if tipoConta == "Salario":
            tarifa = debito * 0.05
            saldo_min = 0
        elif tipoConta == "Comum":
            tarifa = debito * 0.03
            saldo_min = -500
        elif tipoConta == "Plus":
            tarifa = debito * 0.01
            saldo_min = -5000

        #Pega o saldo e subtrai debito e tarifa
        saldo_verifica = float(dados[len(dados) - 1][len(dados[len(dados) - 1])-1]) - debito - tarifa
        #Verifica se o saldo continuará menor que o mínimo possível
        if saldo_verifica > saldo_min:
            saldo_atual = saldo_verifica
            #Fecha o arquivo de usuario
            arquivo.close()
            #Abre o arquivo em append
            arquivo = open(cpf + ".txt", "a")
            #Escreve no arquivo a linha com data e hora, debito, tarifa e saldo atual
            arquivo.write("Data: %s   -   %15.2f                       Tarifa:       %15.2f                    Saldo:     %15.2f\n" % (
            data_e_hora_atuais, debito, tarifa, saldo_atual))
            #Fecha o arquivo de usuário
            arquivo.close()
            print("Débito realizado com sucesso.\n")
        else:
            #Avisos de saldo negativo
            if tipoConta == "Salario":
                print("Não é permitido que um débito deixe seu saldo negativo.\n")
            elif tipoConta == "Comum":
                print("Não é permitido que um débito deixe sua conta com menos de 500 reais negativos.\n")
            elif tipoConta == "Plus":
                print("Não é permitido que um débito deixe sua conta com menos de 5000 reais negativos.\n")
    else:
        print("Senha incorreta, tente efetuar uma nova operação.\n")

#Função para Depósito
def depositaConta():
    #Tarifa será sempre 0 no depósito
    tarifa = 0
    cpf = input("Digite o CPF: ")
    while True:
        # Pega o valor do depósito
        deposito = float(input("Digite o valor a ser depositado: "))
        #Verifica se é maior que 0
        if deposito > 0:
            break
        elif deposito < 0:
            print("Não é possível depositar valores negativos.\n")
        else:
            print("Deposite um valor maior que 0.\n")
    # Abre o arquivo do usuario pelo cpf e lê todas as linhas do mesmo
    arquivo = open(cpf + ".txt", "r")
    for linha in arquivo.readlines():
        linha_sep = linha.split(" ")
        dados.append(linha_sep)

    #Pega o saldo e soma com o depósito
    saldo_atual = float(dados[len(dados) - 1][len(dados[len(dados) - 1])-1]) + deposito
    #Fecha o arquivo do usuario
    arquivo.close()

    #Abre o arquivo de usuario em append
    arquivo = open(cpf + ".txt", "a")
    #Escreve no arquivo a linha com data e hora, deposito, tarifa e saldo atual
    arquivo.write("Data: %s   +   %15.2f                       Tarifa:       %15.2f                    Saldo:     %15.2f\n" %
                  (data_e_hora_atuais, deposito, tarifa, saldo_atual))
    #Fecha o arquivo do usuario
    arquivo.close()
    print("Depósito realizado com sucesso.\n")

def verificaSaldo():
    # Pega o cpf do cliente
    cpf = input("Digite o CPF: ")
    #Pega uma senha
    senha_digitada = input("Digite sua senha: ")
    #Pega a senha do usuario pelo arquivo com senha e cpf
    arq_senha = open("login_" + cpf + ".txt")
    linha_arq_senha = arq_senha.readlines()
    senha = linha_arq_senha[1]
    #Fecha o arquivo de senha
    arq_senha.close()
    #Compara a senha digitada com a do arquivo
    if senha_digitada == senha.strip():
        #Abre o arquivo do usuario e le todas as linhas dele
        arquivo = open(cpf + ".txt", "r")
        for linha in arquivo.readlines():
            # Separa as linhas e passa passa para a list dados
            linha_sep = linha.split(" ")
            dados.append(linha_sep)

        #Imprime o saldo na tela.
        print("O seu saldo é: " + str(dados[len(dados) - 1][len(dados[len(dados) - 1])-1].strip()))
        #Fecha o arquivo de usuario
        arquivo.close()
    else:
        print("Senha incorreta, tente efetuar uma nova operação.\n")

def tirarExtrato():
    # Pega o cpf do cliente
    cpf = input("Digite o CPF: ")
    # Pega uma senha
    senha_digitada = input("Digite sua senha: ")
    # Pega a senha do usuario pelo arquivo com senha e cpf
    arq_senha = open("login_" + cpf + ".txt")
    linha_arq_senha = arq_senha.readlines()
    senha = linha_arq_senha[1]
    # Fecha o arquivo de senha
    arq_senha.close()
    # Compara a senha digitada com a do arquivo
    if senha_digitada == senha.strip():
        # Abre o arquivo do usuario e le todas as linhas dele
        arquivo = open(cpf + ".txt", "r")
        for linha in arquivo.readlines():
            #Imprime todas as linhas na tela
            print(linha.strip())
        print("\n")
        # Fecha o arquivo de usuario
        arquivo.close()
    else:
        print("Senha incorreta, tente efetuar uma nova operação.\n")

#Menu em loop
while True:
    print("1-Novo Cliente")
    print("2-Apaga Cliente")
    print("3-Debita")
    print("4-Depositar")
    print("5-Saldo")
    print("6-Extrato")
    print("0-Sair")
    #Escolha do usuario
    escolha = int(input("Escolha uma Opção: "))
    #Chama as funções de acordo com a escolha
    if escolha == 1:
        criaCliente()
    elif escolha == 2:
        apagaCliente()
    elif escolha == 3:
        debitaConta()
    elif escolha == 4:
        depositaConta()
    elif escolha == 5:
        verificaSaldo()
    elif escolha == 6:
        tirarExtrato()
    elif escolha == 0:
        break
    else:
        print("Opção Inválida.\n")
