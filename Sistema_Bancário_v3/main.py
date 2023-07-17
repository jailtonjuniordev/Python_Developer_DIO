from service import *

def main():
    contas = []
    service = Operacoes(contas)
    service.listar_contas()
    
    while True:
        id_usuario = service.escolher_conta()
        
        if id_usuario is not None:
            if id_usuario >= len(contas) or id_usuario < 0:
                print("O ID informado não está presente acima! Tente novamente.")
                s(2)
                service.limpar_prompt()
            else:
                while True:
                    print("-="*20)
                    print(f"{'Menu':^40}")
                    print("=-"*20)
                    print('''1 - Depositar
2 - Sacar
3 - Extrato
4 - Trocar de Conta
5 - Encerrar Programa''')
                    escolha = int(input("Escolha: "))
                    
                    if escolha == 1 or escolha == 2:
                        service.definir_escolha(escolha=escolha, indice=id_usuario, valor = float(input(f"Digite o valor a ser {'depositado' if escolha == 1 else 'sacar'} R$ ")))
                    elif escolha == 3:
                        service.definir_escolha(escolha=escolha, indice=id_usuario)
                    if escolha == 4:
                        service.limpar_prompt()
                        print("Saindo da conta...")
                        s(2)
                        break

if __name__ == '__main__':
    #main()
    contas = list()
    service = Operacoes(contas)
    service.adicionar_nova_conta("jailton", "123")
    service.definir_escolha(escolha=2, indice=0, valor=50.0)
    print(contas[0].saldo == 50.0)