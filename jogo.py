"""
Este módulo contém a classe Jogo que herda de Entidade.
"""

from entidade import Entidade


class Jogo(Entidade):
    """
    Classe para representar um jogo.
    """

    def __init__(self, nome: str, descricao: str, genero: str, status: str):
        """
        Inicializa um jogo.

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
        Retorna as informações do jogo.
        """
        return (f'Jogo: {self.nome}, Genero: {self.genero}, '
                f'Status: {self.status}, Ativo: {self.ativo}')
