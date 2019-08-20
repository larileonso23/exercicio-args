def imprimir_qualquer_coisa(*args):
    for numero, item in enumerate(args):
        print(str(numero) + '.' + item)

imprimir_qualquer_coisa('maça','abacate','nataçao','batata','bola','lary')