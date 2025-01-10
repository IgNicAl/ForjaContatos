class CPFInvalidoError(Exception):
    pass


class CPF:
    def __init__(self, cpf_input: str):
        self.__cpf = ''.join(filter(str.isdigit, cpf_input))
        if len(self.__cpf) != 11:
            raise CPFInvalidoError('O CPF deve conter exatamente 11 dígitos.')

    def validar(self) -> bool:
        if not self.__cpf.isdigit() or len(self.__cpf) != 11:
            raise CPFInvalidoError('CPF inválido.')
        if self.__cpf == self.__cpf[0] * 11:
            return False
        soma = sum(int(self.__cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10 % 11) % 10
        soma = sum(int(self.__cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (soma * 10 % 11) % 10
        return self.__cpf[-2:] == f'{primeiro_digito}{segundo_digito}'

    def __str__(self):
        return f'{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}'