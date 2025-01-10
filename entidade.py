"""
Este módulo define a classe abstrata Entidade.
"""

from abc import ABC, abstractmethod


class Entidade(ABC):
    """
    Classe abstrata para representar uma entidade.
    """

    def __init__(self, nome: str, ativo: bool = True):
        """
        Inicializa uma entidade.

        Parâmetros:
            nome (str): Nome da entidade.
            ativo (bool): Indica se a entidade está ativa.
        """
        self.nome = nome
        self.ativo = ativo

    @abstractmethod
    def exibir_info(self):
        """
        Método abstrato para exibir informações da entidade.
        """
        raise NotImplementedError("O método exibir_info precisa ser implementado.")

    def atualizar_ativo(self, ativo: bool):
        """
        Atualiza o estado ativo da entidade.

        Parâmetros:
            ativo (bool): Novo estado ativo.
        """
        self.ativo = ativo
