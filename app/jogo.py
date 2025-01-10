"""
Módulo que contém a classe Jogo.
"""

from .entidade import Entidade

class Jogo(Entidade):
    """
    Representa um jogo no estúdio.
    """

    def __init__(self, nome: str, descricao: str, genero: str, status: str):
        """
        Inicializa um objeto Jogo.

        Parâmetros:
            nome (str): Nome do jogo.
            descricao (str): Descrição do jogo.
            genero (str): Gênero do jogo.
            status (str): Status do jogo.
        """
        super().__init__(nome)
        self.descricao = descricao
        self.genero = genero
        self.status = status

    def exibir_info(self):
        """
        Retorna as informações completas do jogo.
        """
        return f'Jogo: {self.nome}, Genero: {self.genero}, Status: {self.status}'
