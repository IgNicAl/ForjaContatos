"""
Interface gráfica para o gerenciamento de jogos e pessoas.
"""

import tkinter as tk
from tkinter import messagebox
from .gamestudio import GameStudio
from .pessoa import Pessoa
from .endereco import Endereco
from .jogo import Jogo

class Interface:
    """
    Classe para gerenciar a interface gráfica do estúdio de jogos.
    Permite adicionar e listar pessoas e jogos.
    """
    def __init__(self, root):
        """
        Inicializa a interface gráfica.
        """
        self.studio = GameStudio("Forja Games")
        self.root = root
        self.root.title("ForjaContatos - Interface Gráfica")

        # Menu principal
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Submenus
        self.pessoa_menu = tk.Menu(self.main_menu, tearoff=0)
        self.jogo_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Pessoa", menu=self.pessoa_menu)
        self.main_menu.add_cascade(label="Jogo", menu=self.jogo_menu)

        # Opções de Pessoa
        self.pessoa_menu.add_command(label="Adicionar Pessoa", command=self.adicionar_pessoa)
        self.pessoa_menu.add_command(label="Listar Pessoas", command=self.listar_pessoas)

        # Opções de Jogo
        self.jogo_menu.add_command(label="Adicionar Jogo", command=self.adicionar_jogo)
        self.jogo_menu.add_command(label="Listar Jogos", command=self.listar_jogos)

    def adicionar_pessoa(self):
        """
        Abre uma janela para adicionar uma pessoa.
        """
        def salvar_pessoa():
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            cep = entry_cep.get()
            numero = entry_numero.get()
            complemento = entry_complemento.get()

            try:
                endereco = Endereco(cep, numero, complemento)
                pessoa = Pessoa(nome, cpf, endereco)
                self.studio.adicionar_pessoa(pessoa)
                messagebox.showinfo("Sucesso", f"Pessoa {nome} adicionada com sucesso!")
                janela.destroy()
            except ValueError as e:
                messagebox.showerror('Erro', str(e))

        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Pessoa")

        tk.Label(janela, text="Nome:").grid(row=0, column=0, pady=5)
        entry_nome = tk.Entry(janela)
        entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(janela, text="CPF:").grid(row=1, column=0, pady=5)
        entry_cpf = tk.Entry(janela)
        entry_cpf.grid(row=1, column=1, pady=5)

        tk.Label(janela, text="CEP:").grid(row=2, column=0, pady=5)
        entry_cep = tk.Entry(janela)
        entry_cep.grid(row=2, column=1, pady=5)

        tk.Label(janela, text="Número:").grid(row=3, column=0, pady=5)
        entry_numero = tk.Entry(janela)
        entry_numero.grid(row=3, column=1, pady=5)

        tk.Label(janela, text="Complemento:").grid(row=4, column=0, pady=5)
        entry_complemento = tk.Entry(janela)
        entry_complemento.grid(row=4, column=1, pady=5)

        tk.Button(janela, text="Salvar", command=salvar_pessoa)\
    .grid(row=5, column=0, columnspan=2, pady=10)

    def listar_pessoas(self):
        """
        Exibe uma janela com a lista de pessoas.
        """
        pessoas = self.studio.listar_pessoas()
        if not pessoas:
            messagebox.showinfo("Lista Vazia", "Nenhuma pessoa cadastrada.")
            return

        janela = tk.Toplevel(self.root)
        janela.title("Lista de Pessoas")

        for pessoa in pessoas:
            tk.Label(janela, text=pessoa).pack()

    def adicionar_jogo(self):
        """
        Abre uma janela para adicionar um jogo.
        """
        def salvar_jogo():
            nome = entry_nome.get()
            descricao = entry_descricao.get()
            genero = entry_genero.get()
            status = entry_status.get()

            try:
                jogo = Jogo(nome, descricao, genero, status)
                self.studio.adicionar_jogo(jogo)
                messagebox.showinfo("Sucesso", f"Jogo {nome} adicionado com sucesso!")
                janela.destroy()
            except ValueError as e:
                messagebox.showerror('Erro', str(e))

        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Jogo")

        tk.Label(janela, text="Nome:").grid(row=0, column=0, pady=5)
        entry_nome = tk.Entry(janela)
        entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(janela, text="Descrição:").grid(row=1, column=0, pady=5)
        entry_descricao = tk.Entry(janela)
        entry_descricao.grid(row=1, column=1, pady=5)

        tk.Label(janela, text="Gênero:").grid(row=2, column=0, pady=5)
        entry_genero = tk.Entry(janela)
        entry_genero.grid(row=2, column=1, pady=5)

        tk.Label(janela, text="Status:").grid(row=3, column=0, pady=5)
        entry_status = tk.Entry(janela)
        entry_status.grid(row=3, column=1, pady=5)

        tk.Button(janela, text="Salvar", command=salvar_jogo)\
    .grid(row=4, column=0, columnspan=2, pady=10)

    def listar_jogos(self):
        """
        Exibe uma janela com a lista de jogos.
        """
        jogos = self.studio.listar_jogos()
        if not jogos:
            messagebox.showinfo("Lista Vazia", "Nenhum jogo cadastrado.")
            return

        janela = tk.Toplevel(self.root)
        janela.title("Lista de Jogos")

        for jogo in jogos:
            tk.Label(janela, text=jogo).pack()

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        main_root = tk.Tk()
        app = Interface(main_root)
        main_root.mainloop()
    else:
        print("Menu Interativo:")
        print("1. Adicionar Pessoa")
        print("2. Adicionar Jogo")
        print("3. Listar Pessoas")
        print("4. Listar Jogos")
        print("5. Salvar Dados")
        print("6. Carregar Dados")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")
        print(f"Opção escolhida: {opcao}")
