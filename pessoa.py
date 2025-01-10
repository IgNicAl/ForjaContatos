"""
Este módulo contém a classe Pessoa, que utiliza CPF e Endereco.
"""

from entidade import Entidade
from cpf import CPF
from endereco import Endereco


class Pessoa(Entidade):
    """
    Classe que representa uma pessoa com CPF e Endereço.
    """

    def __init__(self, nome: str, cpf: str, endereco: Endereco):
        """
        Inicializa um objeto Pessoa.

        Parâmetros:
            nome (str): Nome da pessoa.
            cpf (str): CPF da pessoa.
            endereco (Endereco): Endereço da pessoa.
        """
        super().__init__(nome)
        self.cpf = CPF(cpf)
        self.endereco = endereco

    def exibir_info(self):
        """
        Retorna as informações da pessoa.
        """
        return f'Pessoa: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}'
