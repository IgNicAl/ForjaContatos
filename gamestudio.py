"""
Este módulo contém a classe GameStudio para gerenciar pessoas e jogos.
"""

from pessoa import Pessoa
from jogo import Jogo


class GameStudio:
    """
    Classe para gerenciar um estúdio de jogos.
    """

    def __init__(self, nome: str):
        """
        Inicializa um GameStudio.

        Parâmetros:
            nome (str): Nome do estúdio.
        """
        self.nome = nome
        self.pessoas = []
        self.jogos = []

    def adicionar_pessoa(self, pessoa: Pessoa):
        """
        Adiciona uma pessoa ao estúdio.

        Parâmetros:
            pessoa (Pessoa): Objeto da classe Pessoa.
        """
        self.pessoas.append(pessoa)

    def adicionar_jogo(self, jogo: Jogo):
        """
        Adiciona um jogo ao estúdio.

        Parâmetros:
            jogo (Jogo): Objeto da classe Jogo.
        """
        self.jogos.append(jogo)

    def listar_pessoas(self):
        """
        Retorna uma lista de pessoas cadastradas.
        """
        return [p.exibir_info() for p in self.pessoas]

    def listar_jogos(self):
        """
        Retorna uma lista de jogos cadastrados.
        """
        return [j.exibir_info() for j in self.jogos]
