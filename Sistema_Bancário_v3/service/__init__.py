from entities import Conta
import sys, os
from time import sleep as s

class Operacoes:
    def __init__(self, contas):
        self.contas = contas
        
    def definir_escolha(self, **kw):
        if kw['escolha'] == 1:
            self.limpar_prompt()
            print(self.contas[kw['indice']].depositar(float(kw['valor'])))
            s(1)
            self.limpar_prompt()
        elif kw['escolha'] == 2:
            self.limpar_prompt()
            print(self.contas[kw['indice']].sacar(float(kw['valor'])))
            s(1)
            self.limpar_prompt()
        elif kw['escolha'] == 3:
            self.limpar_prompt()
            self.contas[kw['indice']].extrato()
            s(1)
            self.limpar_prompt()    
        elif kw['escolha'] == 5:
            self.limpar_prompt()
            print("Encerrando Programa...")
            s(1)
            sys.exit()
        
    def cpf_repetido(self, cpf):
        for i in self.contas:
            if cpf.strip() == i.cpf:
                return True
            else:
                return False
            
    def nome_repetido(self, nome_completo):
        for i in self.contas:
            if nome_completo.strip() == i.nome_completo:
                return True
            else:
                return False
        
    def adicionar_nova_conta(self, nome_completo, cpf):
        if len(str(nome_completo).strip()) == 0 or len(cpf.strip()) == 0:
            return print("Nome e/ou CPF não podem ser nulos!")
        elif self.nome_repetido(nome_completo) or self.cpf_repetido(cpf):
            return print("Nome ou CPF não podem constar em nossa base dados.")
        else:
            novaConta = Conta()
            novaConta.nome_completo = nome_completo
            novaConta.cpf = cpf
            self.contas.append(novaConta)
            print(f"{'-='*20}")
            print(f"{'Conta aberta com Sucesso':^40}")
            print(f"{'=-'*20}")
            print(f'{"Dados da Conta":^40}')
            print(f"{'--'*20}")
            print(f'{"Nome Completo":<20}{novaConta.nome_completo}')
            print(f'{"CPF":<20}{novaConta.cpf}')
            print(f'{"Saldo":<20}R$ {novaConta.saldo:.2f}')
            print(f'{"Agência":<20}{novaConta.agencia}')
            print(f"{'--'*20}")
            s(5)
            self.listar_contas()     

    def escolher_conta(self):
        self.listar_contas()
        id_usuario = int(input("[Cadastrar Nova Conta - 999]\n[Fechar Programa - 998]\nEscolha: "))
        if id_usuario == 999:
            self.receber_valores_novos()
        elif id_usuario == 998:
            print("Encerrando programa...")
            s(1)
            sys.exit()
        else:
            return id_usuario
    
    def listar_contas(self):
        if len(self.contas) == 0:
            print(f"{'-='*20}")
            print(f"{'Não existem contas cadastradas!':^40}")
            print(f"{'-='*20}")
            s(2)
            self.limpar_prompt()
            self.receber_valores_novos()
        else:
            print(f"{'-='*20}")
            print(f"{'Contas Disponiveis':^40}")
            print(f"{'-='*20}")
            cont=0
            for i in self.contas:
                print(f'{"Indicie:":<20}{cont}')
                print(f'{"Nome Completo":<20}{i.nome_completo}')
                print(f'{"CPF":<20}{i.cpf}')
                print(f'{"Saldo":<20}R$ {i.saldo:.2f}')
                print(f'{"Agência":<20}{i.agencia}')
                print(f'{"Saques Restantes":<20}{i.LIMITE_SAQUE - i.SAQUE_ATUAL}')
                print(f"{'-='*20}")
                cont += 1
    
    def limpar_prompt(self):
        os.system('clear')
     
    def receber_valores_novos(self):
        print("-="*20)
        print(f"{'Adicionar Nova Conta':^40}")
        print("-="*20)
        nome_completo = str(input("Digite seu Nome Completo: "))
        cpf = str(input("Digite seu CPF: "))
        self.adicionar_nova_conta(nome_completo, cpf)
        self.limpar_prompt()
        return