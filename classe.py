class Carro():

    # Construtor (inicializador)
    def __init__(self, nome:str, combustivel:str):
          self.nome = nome
          self.tipo = combustivel


class Pessoa():

    # Construtor (inicializador)
    def __init__(self, nome:str, idade:int, carro=Carro):
          self.nome = nome
          self.idade = idade
          self.carro = carro

    # método
    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos!\ntenho um {self.carro.nome}, ele se move a {self.carro.tipo}')

# Instanciando - isso é objetos

# Obs: Variáveis criadas a partir da classe pessoa
golbola = Carro('Golbolinhadograu', 'Gasolina')
pessoaGabriel = Pessoa('gabriel', 23, golbola)
pessoaGabriel.apresentar()