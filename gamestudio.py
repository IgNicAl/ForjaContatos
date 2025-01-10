from pessoa import Pessoa
from jogo import Jogo


class GameStudio:
    def __init__(self, nome: str):
        self.nome = nome
        self.pessoas = []
        self.jogos = []

    def adicionar_pessoa(self, pessoa: Pessoa):
        self.pessoas.append(pessoa)

    def adicionar_jogo(self, jogo: Jogo):
        self.jogos.append(jogo)

    def listar_pessoas(self):
        return [p.exibir_info() for p in self.pessoas]

    def listar_jogos(self):
        return [j.exibir_info() for j in self.jogos]