"""
Módulo para representar endereços utilizando CEP.
"""

from .cep import CEP

class Endereco:
    """
    Classe que representa um endereço completo.
    """

    def __init__(self, cep: str, numero: str, complemento: str):
        """
        Inicializa um endereço.

        Parâmetros:
            cep (str): CEP do endereço.
            numero (str): Número da residência.
            complemento (str): Complemento do endereço.
        """
        self.cep = CEP(cep)
        self.numero = numero
        self.complemento = complemento

    def __repr__(self):
        """
        Retorna uma representação textual do endereço.
        """
        return f'{self.cep}, {self.numero}, {self.complemento}'
