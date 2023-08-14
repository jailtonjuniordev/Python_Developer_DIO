from entities import Pessoa
import pytest


class TestPessoa:
    # Tests that the method 'nome_completo.setter' sets the attribute 'nome_completo' correctly
    def test_set_nome_completo(self):
        pessoa = Pessoa()
        pessoa.nome_completo = 'John Doe'
        assert pessoa.nome_completo == 'John Doe'

    # Tests that the method 'nome_completo' returns the correct value of 'nome_completo'
    def test_get_nome_completo(self):
        pessoa = Pessoa()
        pessoa.nome_completo = 'John Doe'
        assert pessoa.nome_completo == 'John Doe'

    # Tests that the method 'cpf.setter' sets the attribute 'cpf' correctly
    def test_set_cpf(self):
        pessoa = Pessoa()
        pessoa.cpf = '12345678901'
        assert pessoa.cpf == '12345678901'

    # Tests that the method 'cpf' returns the correct value of 'cpf'
    def test_get_cpf(self):
        pessoa = Pessoa()
        pessoa.cpf = '12345678901'
        assert pessoa.cpf == '12345678901'

    # Tests that the method 'nome_completo.setter' raises an exception when trying to set an empty 'nome_completo'
    def test_set_empty_nome_completo(self):
        pessoa = Pessoa()
        with pytest.raises(ValueError):
            pessoa.nome_completo = ''

    # Tests that the method 'cpf.setter' raises an exception when trying to set an empty 'cpf'
    def test_set_empty_cpf(self):
        pessoa = Pessoa()
        with pytest.raises(ValueError):
            pessoa.cpf = ''

    # Tests that the method 'nome_completo.setter' sets the attribute 'nome_completo' correctly when it contains special characters
    def test_set_nome_completo_special_characters(self):
        pessoa = Pessoa()
        pessoa.nome_completo = 'John Doe #1'
        assert pessoa.nome_completo == 'John Doe #1'

    # Tests that the method 'cpf.setter' sets the attribute 'cpf' correctly when it contains special characters
    def test_set_cpf_special_characters(self):
        pessoa = Pessoa()
        pessoa.cpf = '123.456.789-01'
        assert pessoa.cpf == '123.456.789-01'