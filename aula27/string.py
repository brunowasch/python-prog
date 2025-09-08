frase = "Aula de programação e o professor está ensinando!"
print(frase)
print(frase.capitalize())
print(frase.title())
print(frase.find('programação'))
frase = frase.replace('o professor', 'alguém')
print(frase)

# Remove palavras do início e do fim da String
palavra = '     teste      '
print(palavra)
print(palavra.strip())
print(palavra.lstrip()) # Left
print(palavra.rstrip()) # Right

letras = 'abcdef'
print(f'{letras} is alpha {letras.isalpha()}')

numeros = '1234577'
print(f'{numeros} is digit {numeros.isdigit()}')

lista = frase.split()
print(lista)

palavra = ' teste '
print(palavra.center(13,'-'))

palavra = 'PaLaVrA'
print(palavra.swapcase())

frase = 'Todos já estão acordados para a hora da merenda!'
print(frase.partition('já'))