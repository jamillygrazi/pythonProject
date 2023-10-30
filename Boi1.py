class Boi:
    def __init__(self, identificacao, peso):
        self.__identificacao = identificacao
        self.__peso = peso

    def get_identificacao(self):
        return self.__identificacao

    def set_identificacao(self, identificacao):
        self.__identificacao = identificacao

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def __str__(self):
        return f"Boi {self.__identificacao}: {self.__peso} kg"

# Inicialize uma lista para armazenar os objetos da classe Boi
bois = []

# Solicite as informações e crie objetos Boi
for i in range(1, 6):
    identificacao = input(f"Digite a identificação do boi {i}: ")
    peso = float(input(f"Digite o peso do boi {i} (em kg): "))
    boi = Boi(identificacao, peso)
    bois.append(boi)

# Encontre o boi mais gordo e o mais magro
boi_mais_gordo = max(bois, key=lambda x: x.get_peso())
boi_mais_magro = min(bois, key=lambda x: x.get_peso())

# Imprima os resultados
print(f"O boi mais gordo é {boi_mais_gordo}. Peso: {boi_mais_gordo.get_peso()} kg")
print(f"O boi mais magro é {boi_mais_magro}. Peso: {boi_mais_magro.get_peso()} kg")
