def listas():

    lista1 = list(range(10))
    lista2 = list(range(1,10))
    lista3 = list(range(1,10,2))
    lista4 = list(range(10,1,-2))
    print(lista1,lista2,lista3,lista4)

    lista1.extend(lista2)
    lista3.append(lista4)

    print(lista1, lista3)

    lista5 = list(['a'] * 3)
    print(lista5)
    print('#'.join(lista5))

    registro = ('Gabriel', 25)
    nome, idade = registro
    print(nome, idade)

    for i, v in enumerate(nome):
        print(i+1, v)