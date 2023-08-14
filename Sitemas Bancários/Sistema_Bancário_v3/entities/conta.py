from entities.pessoa import Pessoa

class Conta(Pessoa):
    def __init__(self):
        self.__LIMITE_SAQUE = 3
        self.__SAQUE_ATUAL = 0
        self.__LIMITE_SAQUE_VALOR = 500.00
        self.__saldo = 0
        self.__agencia = 3909
        self.__movimentacoes = []
        super().__init__()

    def __str__(self):
        return f"Nome: {self.nome_completo}\nCPF: {self.cpf}\nSaldo: R$ {self.saldo}\nMovimentações: {self.__movimentacoes}"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def SAQUE_ATUAL(self):
        return self.__SAQUE_ATUAL

    @SAQUE_ATUAL.setter
    def SAQUE_ATUAL(self, novo_valor):
        self.__SAQUE_ATUAL = novo_valor
        
    @property
    def agencia(self):
        return self.__agencia
    @property
    def LIMITE_SAQUE(self):
        return self.__LIMITE_SAQUE

    def sacar(self, valor_saque):
        if self.SAQUE_ATUAL == self.LIMITE_SAQUE:
            return "Você não possui mais saques disponiveis!"
        elif self.__saldo < valor_saque or valor_saque > self.__LIMITE_SAQUE_VALOR:
            return "Você está excendo o limite de R$ 500,00 por saque e/ou não possui saldo suficiente!"
        else:
            self.SAQUE_ATUAL += 1
            self.saldo -= valor_saque
            self.__movimentacoes.append(valor_saque*-1)
            return "Saque efetuado com Sucesso!"

    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            return "O valor depositado deve ser positivo!"
        else:
            self.saldo += valor_deposito
            self.__movimentacoes.append(valor_deposito)
            return "Deposito efetuado com Sucesso!"

    def extrato(self):
        print(f"{'-='*20}")
        print(f"{'EXTRATO':^40}")
        print(f"{'=-'*20}")
        for i in self.__movimentacoes:
            tipo = 'Depósito' if i > 0 else 'Saque'
            print(f"{tipo:.<30}R$ {abs(i):.2f}")           
        print(f"\n{'Saldo':.<30}R$ {sum(self.__movimentacoes):.2f}\n")
        input("Aperte qualquer tecla para continuar...")


