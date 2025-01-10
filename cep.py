import requests


class CEP:
    def __init__(self, cep: str):
        if not isinstance(cep, str):
            raise ValueError('O CEP deve ser uma string.')
        if not cep.isdigit():
            raise ValueError('O CEP deve conter apenas números.')
        if len(cep) != 8:
            raise ValueError('O CEP deve conter exatamente 8 dígitos.')
        self.__cep = cep
        self.__logradouro = ''
        self.__bairro = ''
        self.__cidade = ''
        self.__estado = ''
        self.__buscar_cep()

    def __repr__(self):
        return (
            f'CEP: {self.__cep}, Rua: {self.__logradouro}, '
            f'Bairro: {self.__bairro}, Cidade: {self.__cidade}, Estado: {self.__estado}'
        )

    def __buscar_cep(self):
        resposta = requests.get(f'https://viacep.com.br/ws/{self.__cep}/json/', timeout=3)
        if resposta.status_code != 200:
            raise ConnectionError('Erro ao acessar a API ViaCEP.')
        dados = resposta.json()
        if 'erro' in dados:
            raise ValueError(f'CEP {self.__cep} não encontrado.')
        self.__logradouro = dados.get('logradouro', '')
        self.__bairro = dados.get('bairro', '')
        self.__cidade = dados.get('localidade', '')
        self.__estado = dados.get('uf', '')
