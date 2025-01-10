from cep import CEP


class Endereco(CEP):
    def __init__(self, cep: str, numero: str, complemento: str):
        super().__init__(cep)
        self.numero = numero
        self.complemento = complemento

    def __repr__(self):
        return f'{self.__logradouro}, {self.numero}, {self.complemento} - {self.__bairro}, {self.__cidade}/{self.__estado}'