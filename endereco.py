"""
Este módulo contém a classe Endereco que utiliza CEP.
"""

from cep import CEP


class Endereco(CEP):
    """
    Classe para representar um endereço que utiliza CEP.
    """

    def __init__(self, cep: str, numero: str, complemento: str):
        """
        Inicializa um objeto Endereco.

        Parâmetros:
            cep (str): CEP do endereço.
            numero (str): Número da residência.
            complemento (str): Complemento do endereço.
        """
        super().__init__(cep)
        self.numero = numero
        self.complemento = complemento

    def __repr__(self):
        """
        Retorna uma representação em string do endereço.
        """
        return (f'{self.__logradouro}, {self.numero}, {self.complemento} - '
                f'{self.__bairro}, {self.__cidade}/{self.__estado}')
