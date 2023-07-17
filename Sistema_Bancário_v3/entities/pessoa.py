class Pessoa:
    def __init__(self):
        self.__nome_completo = None
        self.__cpf = None

    @property
    def nome_completo(self):
        return self.__nome_completo

    @property
    def cpf(self):
        return self.__cpf

    @nome_completo.setter
    def nome_completo(self, novo_nome_completo):
        if len(novo_nome_completo) == 0:
            raise ValueError("Nome completo não pode ser vazio")
        self.__nome_completo = novo_nome_completo

    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 0:
            raise ValueError("CPF não pode ser vazio")
        self.__cpf = novo_cpf