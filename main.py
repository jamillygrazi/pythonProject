from conexão import Database
from generico import Boi, Propriedade
from CRUDGenerico import CRUDGenerico

# Crie instâncias da classe Boi e Propriedade
boi_instancia = Boi("Boi1", 500)
propriedade_instancia = Propriedade("Fazenda ABC", "João da Silva", "12345678901234", "Rua Principal, 123", 100)

# Crie instâncias da classe CRUDGenerico para Bois e Propriedades
crud_boi = CRUDGenerico()
crud_propriedade = CRUDGenerico()

# Crie a instância da classe Database e associe as instâncias de CRUDGenerico
database = Database()
database.crud_boi = crud_boi
database.crud_propriedade = crud_propriedade

# Agora você pode usar a instância da classe Database para acessar e gerenciar os dados de Bois e Propriedades.

class Main:
    def __init__(self):
        self.crud_boi = CRUDGenerico()
        self.crud_propriedade = CRUDGenerico()

    def menu(self):
        while True:
            print("\n### Menu Principal ###")
            print("1. Adicionar Boi")
            print("2. Listar Bois")
            print("3. Atualizar Boi")
            print("4. Deletar Boi")
            print("5. Adicionar Propriedade")
            print("6. Listar Propriedades")
            print("7. Atualizar Propriedade")
            print("8. Deletar Propriedade")
            print("9. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.adicionar_boi()
            elif escolha == "2":
                self.listar_bois()
            elif escolha == "3":
                self.atualizar_boi()
            elif escolha == "4":
                self.deletar_boi()
            elif escolha == "5":
                self.adicionar_propriedade()
            elif escolha == "6":
                self.listar_propriedades()
            elif escolha == "7":
                self.atualizar_propriedade()
            elif escolha == "8":
                self.deletar_propriedade()
            elif escolha == "9":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def adicionar_boi(self):
        identificacao = input("Identificação do Boi: ")
        peso = float(input("Peso do Boi (em kg): "))
        boi = Boi(identificacao, peso)
        self.crud_boi.criar(boi)
        print("Boi adicionado com sucesso.")

    def listar_bois(self):
        bois = self.crud_boi.listar()
        if bois:
            for index, boi in enumerate(bois):
                print(f"{index}. {boi}")
        else:
            print("Nenhum boi cadastrado.")

    def atualizar_boi(self):
        self.listar_bois()
        index = int(input("Digite o índice do Boi que deseja atualizar: "))
        bois = self.crud_boi.listar()
        if 0 <= index < len(bois):
            novo_identificacao = input("Nova identificação do Boi: ")
            novo_peso = float(input("Novo peso do Boi (em kg): "))
            novo_boi = Boi(novo_identificacao, novo_peso)
            self.crud_boi.atualizar(index, novo_boi)
            print("Boi atualizado com sucesso.")
        else:
            print("Índice inválido.")

    def deletar_boi(self):
        self.listar_bois()
        index = int(input("Digite o índice do Boi que deseja deletar: "))
        bois = self.crud_boi.listar()
        if 0 <= index < len(bois):
            self.crud_boi.deletar(index)
            print("Boi deletado com sucesso.")
        else:
            print("Índice inválido.")

    def adicionar_propriedade(self):
        nome = input("Nome da Propriedade: ")
        proprietario = input("Proprietário: ")
        cnpj = input("CNPJ: ")
        endereco = input("Endereço: ")
        hectares = float(input("Hectares: "))
        propriedade = Propriedade(nome, proprietario, cnpj, endereco, hectares)
        self.crud_propriedade.criar(propriedade)
        print("Propriedade adicionada com sucesso.")

    def listar_propriedades(self):
        propriedades = self.crud_propriedade.listar()
        if propriedades:
            for index, propriedade in enumerate(propriedades):
                print(f"{index}. {propriedade}")
        else:
            print("Nenhuma propriedade cadastrada.")

    def atualizar_propriedade(self):
        self.listar_propriedades()
        index = int(input("Digite o índice da Propriedade que deseja atualizar: "))
        propriedades = self.crud_propriedade.listar()
        if 0 <= index < len(propriedades):
            novo_nome = input("Novo nome da Propriedade: ")
            novo_proprietario = input("Novo proprietário: ")
            novo_cnpj = input("Novo CNPJ: ")
            novo_endereco = input("Novo endereço: ")
            novo_hectares = float(input("Novos hectares: "))
            nova_propriedade = Propriedade(novo_nome, novo_proprietario, novo_cnpj, novo_endereco, novo_hectares)
            self.crud_propriedade.atualizar(index, nova_propriedade)
            print("Propriedade atualizada com sucesso.")
        else:
            print("Índice inválido.")

    def deletar_propriedade(self):
        self.listar_propriedades()
        index = int(input("Digite o índice da Propriedade que deseja deletar: "))
        propriedades = self.crud_propriedade.listar()
        if 0 <= index < len(propriedades):
            self.crud_propriedade.deletar(index)
            print("Propriedade deletada com sucesso.")
        else:
            print("Índice inválido.")


if __name__ == "__main__":
    main_program = Main()
    main_program.menu()

