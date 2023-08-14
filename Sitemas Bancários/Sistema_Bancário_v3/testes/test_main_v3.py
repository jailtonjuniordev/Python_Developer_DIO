from service import *
import pytest

class TestMain:
    # Tests selecting an existing account and depositing money
    def test_existing_account_deposit(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        service.listar_contas()
        id_usuario = 0
        service.definir_escolha(escolha=1, indice=id_usuario, valor=100.0)
        assert contas[id_usuario].saldo == 100.0

    # Tests selecting an existing account and withdrawing money
    def test_existing_account_withdraw(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        service.listar_contas()
        id_usuario = 0
        service.definir_escolha(escolha=1, indice=id_usuario, valor=100.0)
        service.definir_escolha(escolha=2, indice=id_usuario, valor=50.0)
        assert contas[id_usuario].saldo == 50.0

    # Tests selecting an existing account and checking the account statement
    def test_existing_account_statement(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        service.listar_contas()
        id_usuario = 0
        service.definir_escolha(escolha=1, indice=id_usuario, valor=100.0)
        assert contas[id_usuario].saldo == 100.0

    # Tests exiting the account and returning to the account selection menu
    def test_exit_account_selection(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        service.listar_contas()
        id_usuario = 0
        assert service.definir_escolha(escolha=4, indice=id_usuario) is None

    # Tests exiting the program from the account selection menu
    def test_exit_program(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        with pytest.raises(SystemExit):
            service.definir_escolha(escolha=5, indice=0)

    # Tests selecting a non-existent account
    def test_nonexistent_account(self):
        contas = []
        service = Operacoes(contas)
        service.adicionar_nova_conta("jailton", "123")
        service.listar_contas()
        id_usuario = 1
        with pytest.raises(IndexError):
            service.definir_escolha(escolha=1, indice=id_usuario, valor=100.0)