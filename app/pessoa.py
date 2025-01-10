"""
Módulo que contém a classe Pessoa.
"""

from app.entidade import Entidade
from app.cpf import CPF
from app.endereco import Endereco

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
