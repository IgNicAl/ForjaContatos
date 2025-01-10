from entidade import Entidade


class Jogo(Entidade):
    def __init__(self, nome: str, descricao: str, genero: str, status: str):
        super().__init__(nome)
        self.descricao = descricao
        self.genero = genero
        self.status = status

    def exibir_info(self):
        return f'Jogo: {self.nome}, Genero: {self.genero}, Status: {self.status}, Ativo: {self.ativo}'
