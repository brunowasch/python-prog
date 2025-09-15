class Pessoa:
    # Constrututor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')

pessoa_um = Pessoa('Jonas', 18)
pessoa_um.apresentar()

class Aluno(Pessoa):
    # Chama o construtor da superclasse
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def apresentar(self):
        print(f'Nome: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}')

aluno_um = Aluno('Jonas', 18, 12345)
aluno_um.apresentar()