import os
from time import sleep as s

LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500.0
movimentacoes = []
conta = {
    "saldo": 0.0,
    "saques": 0,
    "extrato": movimentacoes
}

def main():
    while True:
        print("MENU")
        print("---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        
        escolha = int(input("Escolha: "))
    
        if (escolha == 1):
            limpar_prompt()
            conta["saldo"] += depositar()
            limpar_prompt()
        elif (escolha == 2):
            limpar_prompt()
            conta["saldo"] -= sacar()
            limpar_prompt()
        elif (escolha == 3):
            limpar_prompt()
            extrato()
            limpar_prompt()
        elif (escolha == 4):
            limpar_prompt()
            print("Encerrando o programa...")
            s(2)
            break

def sacar():
    while True:
        print("SAQUE")
        print("---")
        if(conta["saques"] >= LIMITE_SAQUE):
            print("Você excedeu o limite de saques diários!")
            s(2)
            return 0
        valor = float(input("Digite o valor que deseja sacar [Limite de R$ 500.00] R$ "))
        if(conta["saldo"] >= valor and valor > 0 and valor <= VALOR_LIMITE_SAQUE):
            movimentacoes.append((valor*-1))
            conta["saques"] += 1
            return valor
        else:
            print("Saldo não disponivel em conta para saque, excede o valor limite de R$ 500,00 por saque ou é menor do que 0!")
            print("Você será redirecionado ao MENU")
            s(2)
            limpar_prompt()
            return 0

def depositar():
    while True:
        print("DEPOSITO")
        print("---")
        valor = float(input("Digite o valor que deseja depositar R$ "))
        if(valor > 0):
            movimentacoes.append(valor)
            return valor
        else:
            print("Valor deve ser positivo!")
            print("Depósito falhou! você será redirecionado ao MENU")
            s(2)
            limpar_prompt()
            return 0
        
def extrato():
    print("EXTRATO")
    print("---")
    for i in range(len(movimentacoes)):
        print(f"{'Depósito' if movimentacoes[i] > 0 else 'Saque' } . . . R$ {movimentacoes[i]}")
    print("---")
    print(f"Saldo Atual: R$ {conta['saldo']}")
    input("Aperte qualquer tecla para continuar...")

def limpar_prompt():
    os.system('clear')
    
if __name__ == '__main__':
    main()