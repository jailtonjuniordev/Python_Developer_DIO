import os
from time import sleep as s
from random import randint as r

LIMITE_SAQUE = 3
global id_usuario
VALOR_LIMITE_SAQUE = 500.0
contas = list()

def menu(id_usuario):
    while True:
        print("MENU")
        print("---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair da Conta")
        print("5 - Fechar programa")

        escolha = int(input("Escolha: "))

        if (escolha == 1):
            limpar_prompt()
            contas[id_usuario]["saldo"] += depositar(id_usuario)
            limpar_prompt()
        elif (escolha == 2):
            limpar_prompt()
            contas[id_usuario]["saldo"] -= sacar(id_usuario)
            limpar_prompt()
        elif (escolha == 3):
            limpar_prompt()
            extrato(id_usuario)
            limpar_prompt()
        elif (escolha == 4):
            limpar_prompt()
            listar_contas()
        elif (escolha == 5):
            limpar_prompt()
            print("Encerrando o programa...")
            s(2)
            break

def main():
    if len(contas) == 0:
        criar_usuario()
    else:
        listar_contas()

def sacar(id_usuario):
    while True:
        print("SAQUE")
        print("---")
        if(contas[id_usuario]["saques"] == LIMITE_SAQUE):
            print("Você excedeu o limite de saques diários!")
            s(2)
            return 0
        valor = float(input("Digite o valor que deseja sacar [Limite de R$ 500.00] R$ "))
        if(contas[id_usuario]["saldo"] >= valor and valor > 0 and valor <= VALOR_LIMITE_SAQUE):
            contas[id_usuario]["extrato"].append((valor*-1))
            contas[id_usuario]["saques"] += 1
            return valor
        else:
            print("Saldo não disponivel em conta para saque, excede o valor limite de R$ 500,00 por saque ou é menor do que 0!")
            print("Você será redirecionado ao MENU")
            s(2)
            limpar_prompt()
            return 0

def depositar(id_usuario):
    while True:
        print("DEPOSITO")
        print("---")
        valor = float(input("Digite o valor que deseja depositar R$ "))
        if(valor > 0):
            contas[id_usuario]["extrato"].append(valor)
            return valor
        else:
            print("Valor deve ser positivo!")
            print("Depósito falhou! você será redirecionado ao MENU")
            s(2)
            limpar_prompt()
            return 0
        
def extrato(id_usuario):
    print("EXTRATO")
    print("---")
    for i in contas[id_usuario]["extrato"]:
        print(f"{'Depósito' if i > 0 else 'Saque' } . . . R$ {i}")
    print("---")
    print(f"Saldo Atual: R$ {sum(contas[id_usuario]['extrato'])}")
    input("Aperte qualquer tecla para continuar...")

def verificar_cpf():
    while True:
        cpf = str(input("Digite seu CPF: "))
        
        for i in range(len(contas)):
            if cpf == contas[i]["cpf"]:
                return [True]

        
        return [False, cpf]

def criar_usuario():
    conta = {
    "nome_usuario": "",
    "cpf": "",
    "conta_corrente": "",
    "saldo": 0.0,
    "saques": 0,
    "extrato": []
    }
    contas.append(conta)
    contas[-1]["nome_usuario"] = str(input("Digite seu nome completo: "))

    contas[-1]["cpf"] = verificar_cpf()[1]
    
    contas[-1]["conta_corrente"] = f'{r(5, 10)}{r(7, 8)}{r(10, 15)}-{r(5, 10) + r(7, 8) + r(10, 15)}'
    limpar_prompt()
    print(f'Sua conta foi aberta! aqui abaixo estão os dados dela!')
    s(1)
    print('---')
    print('Nome:', contas[-1]["nome_usuario"])
    print('CPF:', contas[-1]["cpf"])
    print('Número da Conta:', contas[-1]["conta_corrente"])
    print('Saldo: R$', contas[-1]["saldo"])
    print('Saques Restantes', contas[-1]["saques"])
    print('---')
    input("Aperte qualquer botão para voltar ao menu principal")
    s(1)
    limpar_prompt()
    listar_contas()

def listar_contas():
    print('SELECIONAR CONTA')
    print('---')
    print("Para Cadastrar uma nova conta digite 999")
    for i in range(len(contas)):
        print('---')
        print(f'Indice: {i}')
        print(f'Nome do Usuario: {contas[i]["nome_usuario"]}')
        print(f'CPF: {contas[i]["cpf"]}')
        print('---')
    escolha = int(input("Escolha algum dos indices acima: "))
    
    if escolha == 999:
        criar_usuario()
    else:
        id_usuario = escolha
        menu(id_usuario)
    
def limpar_prompt():
    os.system('clear')
    
if __name__ == '__main__':
    main()

