"""
Módulo para gerenciamento de estúdios de jogos.
"""

import json
from .pessoa import Pessoa
from .jogo import Jogo

class GameStudio:
    """
    Representa um estúdio de jogos, permitindo gerenciar listas de pessoas e jogos.
    """

    def __init__(self, nome: str):
        """
        Inicializa o estúdio de jogos.

        Parâmetros:
            nome (str): Nome do estúdio de jogos.
        """
        self.nome = nome
        self.pessoas = []
        self.jogos = []

    def adicionar_pessoa(self, pessoa: Pessoa):
        """
        Adiciona uma nova pessoa ao estúdio.

        Parâmetros:
            pessoa (Pessoa): Objeto da classe Pessoa a ser adicionado.
        """
        self.pessoas.append(pessoa)

    def adicionar_jogo(self, jogo: Jogo):
        """
        Adiciona um novo jogo ao estúdio.

        Parâmetros:
            jogo (Jogo): Objeto da classe Jogo a ser adicionado.
        """
        self.jogos.append(jogo)

    def listar_pessoas(self):
        """
        Retorna uma lista de informações sobre todas as pessoas cadastradas no estúdio.

        Retorno:
            list[str]: Lista contendo representações textuais de cada pessoa.
        """
        return [p.exibir_info() for p in self.pessoas]

    def listar_jogos(self):
        """
        Retorna uma lista de informações sobre todos os jogos cadastrados no estúdio.

        Retorno:
            list[str]: Lista contendo representações textuais de cada jogo.
        """
        return [j.exibir_info() for j in self.jogos]

    def salvar_dados_json(self, arquivo='dados.json'):
        """
        Salva as listas de pessoas e jogos em um arquivo JSON.

        Parâmetros:
            arquivo (str): Nome do arquivo onde os dados serão salvos. Padrão é 'dados.json'.
        """
        dados = {
            'pessoas': [
                {'nome': p.nome, 'cpf': str(p.cpf), 'endereco': str(p.endereco)}
                for p in self.pessoas
            ],
            'jogos': [
                {'nome': j.nome, 'descricao': j.descricao, 'genero': j.genero, 'status': j.status}
                for j in self.jogos
            ],
        }
        with open(arquivo, 'w', encoding='utf-8') as f:  # Adicionando encoding
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados_json(self, arquivo='dados.json'):
        """
        Carrega os dados de pessoas e jogos de um arquivo JSON.

        Parâmetros:
            arquivo (str): Nome do arquivo de onde os dados serão carregados. Padrão é 'dados.json'.
        """
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:  # Adicionando encoding
                dados = json.load(f)
            self.pessoas = [Pessoa(**p) for p in dados['pessoas']]
            self.jogos = [Jogo(**j) for j in dados['jogos']]
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar o arquivo '{arquivo}'.")
