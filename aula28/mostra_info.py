def mostra_info(**info):
    '''Função que recebe um número variável de parâmetros'''
    for chave, valor in info.items():
        print(f'{chave}:{valor}')

mostra_info(nome = 'Jonas', idade = 18, altura = 1.8, e_mail = 'jonas@gmail.com')

print(mostra_info.__doc__)