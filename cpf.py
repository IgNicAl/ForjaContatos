"""
Este módulo contém a classe CPF para manipulação e validação de CPFs.
"""


class CPFInvalidoError(Exception):
    """
    Exceção levantada quando um CPF é inválido.
    """
    # Não é necessário um `pass` aqui.
    ...


class CPF:
    """
    Classe para manipular e validar CPFs.
    """

    def __init__(self, cpf_input: str):
        """
        Inicializa um objeto CPF.

        Parâmetros:
            cpf_input (str): CPF no formato string.
        """
        self.__cpf = ''.join(filter(str.isdigit, cpf_input))
        if len(self.__cpf) != 11:
            raise CPFInvalidoError('O CPF deve conter exatamente 11 dígitos.')

    def validar(self) -> bool:
        """
        Valida o CPF utilizando o algoritmo de validação de dígitos verificadores.

        Retorno:
            bool: True se o CPF for válido, False caso contrário.
        """
        if self.__cpf == self.__cpf[0] * 11:
            return False
        soma = sum(int(self.__cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10 % 11) % 10
        soma = sum(int(self.__cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (soma * 10 % 11) % 10
        return self.__cpf[-2:] == f'{primeiro_digito}{segundo_digito}'

    def __str__(self):
        """
        Retorna o CPF formatado.
        """
        return f'{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}'
