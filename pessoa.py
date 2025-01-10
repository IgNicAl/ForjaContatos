from entidade import Entidade
from cpf import CPF
from endereco import Endereco


class Pessoa(Entidade):
    def __init__(self, nome: str, cpf: str, endereco: Endereco):
        super().__init__(nome)
        self.cpf = CPF(cpf)
        self.endereco = endereco

    def exibir_info(self):
        return f'Pessoa: {self.nome}, CPF: {self.cpf}, Endereco: {self.endereco}'