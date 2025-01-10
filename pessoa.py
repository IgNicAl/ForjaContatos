"""
Módulo que contém a classe Pessoa.
"""

from entidade import Entidade
from cpf import CPF
from endereco import Endereco

class Pessoa(Entidade):
    """
    Representa uma pessoa física.
    """

    def __init__(self, nome: str, cpf: str, endereco: Endereco):
        """
        Inicializa uma pessoa física.

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
        Retorna as informações completas da pessoa.
        """
        return f'Pessoa: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}'
