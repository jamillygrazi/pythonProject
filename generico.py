class CRUD:
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

class Boi:
    def __init__(self, identificacao, peso):
        self.identificacao = identificacao
        self.peso = peso

    def __str__(self):
        return f"Identificação do Boi: {self.identificacao}\nPeso: {self.peso} kg"


class Propriedade:
    def __init__(self, nome, proprietario, cnpj, endereco, hectares):
        self.nome = nome
        self.proprietario = proprietario
        self.cnpj = cnpj
        self.endereco = endereco
        self.hectares = hectares

    def __str__(self):
        return f"Nome da Propriedade: {self.nome}\nProprietário: {self.proprietario}\nCNPJ: {self.cnpj}\nEndereço: {self.endereco}\nHectares: {self.hectares}"

# Exemplo de uso da classe CRUD com objetos "Boi"
crud_bois = CRUD()
crud_bois.criar(Boi("A1", 500))
crud_bois.criar(Boi("B2", 600))

# Exemplo de uso da classe CRUD com objetos "Propriedade"
crud_propriedades = CRUD()
crud_propriedades.criar(Propriedade("Fazenda ABC", "João da Silva", "12345678901234", "Rua Principal, 123", 100))
crud_propriedades.criar(Propriedade("Sítio XYZ", "Maria Oliveira", "98765432104321", "Av. Secundária, 456", 50))

# Listar e imprimir objetos
print("Lista de Bois:")
for boi in crud_bois.listar():
    print(boi)

print("\nLista de Propriedades:")
for propriedade in crud_propriedades.listar():
    print(propriedade)
