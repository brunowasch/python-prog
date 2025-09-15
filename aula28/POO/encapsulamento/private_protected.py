class Pessoa:
    # Constrututor
    def __init__(self, nome, altura):
        self.__nome = nome  # Private (2 underlines)
        self._altura = altura # Protected (1 underline)

# Não podemos acessar um atributo privado diretamente
pessoa_um = Pessoa('Jonas', 180)
print(pessoa_um._Pessoa__nome)
print(pessoa_um._altura)