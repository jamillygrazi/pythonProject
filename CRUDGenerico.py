class CRUDGenerico:
    def __init__(self):
        self.objetos = []

    def criar(self, objeto):
        self.objetos.append(objeto)

    def ler(self, index):
        if 0 <= index < len(self.objetos):
            return self.objetos[index]
        else:
            return None

    def atualizar(self, index, novo_objeto):
        if 0 <= index < len(self.objetos):
            self.objetos[index] = novo_objeto

    def deletar(self, index):
        if 0 <= index < len(self.objetos):
            del self.objetos[index]

    def listar(self):
        return self.objetos
