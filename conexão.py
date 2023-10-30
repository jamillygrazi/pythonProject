from Boi1 import Boi
from generico import Propriedade

from CRUDGenerico import CRUDGenerico

class Database:
    def __init__(self):
        self.crud_boi = CRUDGenerico()
        self.crud_propriedade = CRUDGenerico()

    def adicionar_boi(self, identificacao, peso):
        boi = Boi(identificacao, peso)
        self.crud_boi.criar(boi)

    def listar_bois(self):
        return self.crud_boi.listar()

    def atualizar_boi(self, index, novo_identificacao, novo_peso):
        bois = self.crud_boi.listar()
        if 0 <= index < len(bois):
            novo_boi = Boi(novo_identificacao, novo_peso)
            self.crud_boi.atualizar(index, novo_boi)

    def deletar_boi(self, index):
        bois = self.crud_boi.listar()
        if 0 <= index < len(bois):
            self.crud_boi.deletar(index)

    def adicionar_propriedade(self, nome, proprietario, cnpj, endereco, hectares):
        propriedade = Propriedade(nome, proprietario, cnpj, endereco, hectares)
        self.crud_propriedade.criar(propriedade)

    def listar_propriedades(self):
        return self.crud_propriedade.listar()

    def atualizar_propriedade(self, index, novo_nome, novo_proprietario, novo_cnpj, novo_endereco, novo_hectares):
        propriedades = self.crud_propriedade.listar()
        if 0 <= index < len(propriedades):
            nova_propriedade = Propriedade(novo_nome, novo_proprietario, novo_cnpj, novo_endereco, novo_hectares)
            self.crud_propriedade.atualizar(index, nova_propriedade)

    def deletar_propriedade(self, index):
        propriedades = self.crud_propriedade.listar()
        if 0 <= index < len(propriedades):
            self.crud_propriedade.deletar(index)

    def listar_todos_os_bois(self):
        return self.crud_boi.listar()

    def listar_todas_as_propriedades(self):
        return self.crud_propriedade.listar()

# Inicialize a classe Database
database = Database()

# Exemplo de uso:
# database.adicionar_boi("Boi1", 500)
# database.adicionar_propriedade("Propriedade1", "Proprietario1", "12345", "Endereco1", 100)
# database.listar_bois()
# database.listar_propriedades()

