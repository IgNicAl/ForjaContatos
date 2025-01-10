"""
Este módulo contém a classe CEP para manipulação de códigos postais.
"""

import requests


class CEP:
    """
    Classe para buscar e manipular informações de um CEP.
    """

    def __init__(self, cep: str):
        """
        Inicializa um objeto CEP.

        Parâmetros:
            cep (str): Código postal de 8 dígitos.
        """
        if not isinstance(cep, str):
            raise ValueError('O CEP deve ser uma string.')
        if not cep.isdigit() or len(cep) != 8:
            raise ValueError('O CEP deve conter exatamente 8 dígitos.')
        self.__cep = cep
        self.__logradouro = ''
        self.__bairro = ''
        self.__cidade = ''
        self.__estado = ''
        self.__buscar_cep()

    def __buscar_cep(self):
        """
        Busca informações do CEP na API ViaCEP.
        """
        resposta = requests.get(f'https://viacep.com.br/ws/{self.__cep}/json/')
        if resposta.status_code != 200:
            raise ConnectionError('Erro ao acessar a API ViaCEP.')
        dados = resposta.json()
        if 'erro' in dados:
            raise ValueError(f'CEP {self.__cep} não encontrado.')
        self.__logradouro = dados.get('logradouro', '')
        self.__bairro = dados.get('bairro', '')
        self.__cidade = dados.get('localidade', '')
        self.__estado = dados.get('uf', '')

    def __repr__(self):
        """
        Retorna uma representação em string do CEP.
        """
        return (f'CEP: {self.__cep}, Rua: {self.__logradouro}, '
                f'Bairro: {self.__bairro}, Cidade: {self.__cidade}, Estado: {self.__estado}')
