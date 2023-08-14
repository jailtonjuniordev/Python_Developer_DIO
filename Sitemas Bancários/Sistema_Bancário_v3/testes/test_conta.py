from entities import Conta
import pytest

class TestConta:
    # Tests that depositing a positive value increases the account balance
    def test_deposit_positive_value(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        assert conta.saldo == 1000

    # Tests that withdrawing a value within the limit decreases the account balance
    def test_withdraw_within_limit(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        conta.sacar(100)
        assert conta.saldo == 900

    # Tests that withdrawing the maximum allowed value decreases the account balance
    def test_withdraw_maximum_allowed_value(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        conta.sacar(500)
        assert conta.saldo == 500

    # Tests that printing the account information returns the expected string
    def test_print_account_information(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        assert str(
            conta) == "Nome: Fulano de Tal\nCPF: 123.456.789-00\nSaldo: R$ 1000\nMovimentações: [1000]"

    # Tests that withdrawing a value above the limit returns an error message
    def test_withdraw_above_limit(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        assert conta.sacar(
            600) == "Você está excendo o limite de R$ 500,00 por saque e/ou não possui saldo suficiente!"

    # Tests that withdrawing a value greater than the balance returns an error message
    def test_withdraw_greater_than_balance(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        assert conta.sacar(
            2000) == "Você está excendo o limite de R$ 500,00 por saque e/ou não possui saldo suficiente!"

    # Tests that depositing a negative value returns an error message
    def test_deposit_negative_value(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        assert conta.depositar(-100) == "O valor depositado deve ser positivo!"

    # Tests that setting an empty name returns an error message
    def test_set_empty_name(self):
        conta = Conta()
        with pytest.raises(ValueError):
            conta.nome_completo = ''

    # Tests that setting an empty CPF returns an error message
    def test_set_empty_cpf(self):
        conta = Conta()
        with pytest.raises(ValueError):
            conta.cpf = ''

    # Tests that withdrawing the maximum allowed value plus one cent returns an error message
    def test_withdraw_maximum_allowed_value_plus_one_cent(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(1000)
        assert conta.sacar(
            500.01) == "Você está excendo o limite de R$ 500,00 por saque e/ou não possui saldo suficiente!"

    # Tests that withdrawing the maximum allowed number of times returns an error message
    def test_withdraw_maximum_allowed_number_of_times(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(5000)
        conta.sacar(500)
        conta.sacar(500)
        conta.sacar(500)
        assert conta.sacar(500) == "Você não possui mais saques disponiveis!"

    # Tests that depositing the maximum allowed value increases the account balance
    def test_deposit_maximum_allowed_value(self):
        conta = Conta()
        conta.nome_completo = 'Fulano de Tal'
        conta.cpf = '123.456.789-00'
        conta.depositar(500)
        assert conta.saldo == 500
