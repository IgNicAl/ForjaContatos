from abc import ABC, abstractmethod


class Entidade(ABC):
    def __init__(self, nome: str, ativo: bool = True):
        self.nome = nome
        self.ativo = ativo

    @abstractmethod
    def exibir_info(self):
        pass

    def atualizar_ativo(self, ativo: bool):
        self.ativo = ativo
