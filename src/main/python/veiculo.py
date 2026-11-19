class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def acelerar(self):
        print("O veículo está acelerando.")

    def frear(self):
        print("O veículo está freando.")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.__num_portas = num_portas

    def abrir_porta(self):
        print("Abrindo porta do carro.")

    def acelerar(self):
        print("O carro está acelerando rapidamente.")
    

