"""
Módulo principal do sistema ForjaContatos.

Este módulo pode ser executado em dois modos:
1. Interface gráfica: Inicia uma GUI para gerenciar pessoas e jogos.
2. Menu interativo: Permite gerenciar pessoas e jogos diretamente pelo terminal.

Argumentos:
    --gui: Inicia o modo de interface gráfica.

"""

import sys
import tkinter as tk
from app.interface import Interface
from app.endereco import Endereco
from app.pessoa import Pessoa
from app.jogo import Jogo
from app.gamestudio import GameStudio

# Verifica se o programa deve executar a interface gráfica ou o menu no terminal
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        # Executa a interface gráfica
        root = tk.Tk()
        app = Interface(root)
        root.mainloop()
    else:
        # Inicializa o estúdio de jogos para o menu interativo
        studio = GameStudio("Forja Games")

        while True:
            # Exibe o menu interativo
            print("\nMenu Interativo:")
            print("1. Adicionar Pessoa")
            print("2. Adicionar Jogo")
            print("3. Listar Pessoas")
            print("4. Listar Jogos")
            print("5. Salvar Dados")
            print("6. Carregar Dados")
            print("7. Sair")

            # Solicita uma opção do usuário
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                # Adiciona uma nova pessoa ao estúdio
                nome = input("Nome da pessoa: ")
                cpf = input("CPF da pessoa: ")
                cep = input("CEP: ")
                numero = input("Número: ")
                complemento = input("Complemento: ")
                endereco = Endereco(cep, numero, complemento)
                pessoa = Pessoa(nome, cpf, endereco)
                studio.adicionar_pessoa(pessoa)

            elif opcao == "2":
                # Adiciona um novo jogo ao estúdio
                nome = input("Nome do jogo: ")
                descricao = input("Descrição: ")
                genero = input("Gênero: ")
                status = input("Status: ")
                jogo = Jogo(nome, descricao, genero, status)
                studio.adicionar_jogo(jogo)

            elif opcao == "3":
                # Lista as pessoas cadastradas no estúdio
                print("Pessoas cadastradas:")
                for info in studio.listar_pessoas():
                    print(info)

            elif opcao == "4":
                # Lista os jogos cadastrados no estúdio
                print("Jogos cadastrados:")
                for info in studio.listar_jogos():
                    print(info)

            elif opcao == "5":
                # Salva os dados em um arquivo JSON
                arquivo = input("Nome do arquivo para salvar: ")
                studio.salvar_dados_json(arquivo)

            elif opcao == "6":
                # Carrega os dados de um arquivo JSON
                arquivo = input("Nome do arquivo para carregar: ")
                studio.carregar_dados_json(arquivo)

            elif opcao == "7":
                # Encerra o programa
                print("Saindo...")
                break

            else:
                # Informa que a opção é inválida
                print("Opção inválida. Tente novamente.")
