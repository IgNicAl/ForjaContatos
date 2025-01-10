"""
Programa principal para gerenciar um estúdio de jogos.
"""

from endereco import Endereco
from pessoa import Pessoa
from jogo import Jogo
from gamestudio import GameStudio

if __name__ == '__main__':
    studio = GameStudio('Forja Games')

    while True:
        print('\nMenu Interativo:')
        print('1. Adicionar Pessoa')
        print('2. Adicionar Jogo')
        print('3. Listar Pessoas')
        print('4. Listar Jogos')
        print('5. Salvar Dados')
        print('6. Carregar Dados')
        print('7. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Nome da pessoa: ')
            cpf = input('CPF da pessoa: ')
            cep = input('CEP: ')
            numero = input('Número: ')
            complemento = input('Complemento: ')
            endereco = Endereco(cep, numero, complemento)
            pessoa = Pessoa(nome, cpf, endereco)
            studio.adicionar_pessoa(pessoa)

        elif opcao == '2':
            nome = input('Nome do jogo: ')
            descricao = input('Descrição: ')
            genero = input('Gênero: ')
            status = input('Status: ')
            jogo = Jogo(nome, descricao, genero, status)
            studio.adicionar_jogo(jogo)

        elif opcao == '3':
            print('Pessoas cadastradas:')
            for info in studio.listar_pessoas():
                print(info)

        elif opcao == '4':
            print('Jogos cadastrados:')
            for info in studio.listar_jogos():
                print(info)

        elif opcao == '5':
            arquivo = input('Nome do arquivo para salvar: ')
            studio.salvar_dados_json(arquivo)

        elif opcao == '6':
            arquivo = input('Nome do arquivo para carregar: ')
            studio.carregar_dados_json(arquivo)

        elif opcao == '7':
            print('Saindo...')
            break

        else:
            print('Opção inválida. Tente novamente.')
