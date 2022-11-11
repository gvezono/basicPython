def dicionarios():

    linguas = {'br':'portugues-br', 'eua':'ingles'}
    print(linguas)
    linguas['es'] = 'espanhol'
    print(linguas)
    for chave, valor in linguas.items():
        print(chave, valor)
    linguas.pop('es')
    print(linguas)

def parametros(nome, sobrenome = 'default'):
    #caso o usuário não forneça um sobrenome, a função utilizará o valor default fornecido
    saudacao = f"Olá {nome} {sobrenome} !"
    return print(saudacao)

def exercicio1_conta_caracteres(string_passada):

    string_ordenada = sorted(string_passada)
    caracter_anterior = string_ordenada[0]
    contador = 1
    for caracter in string_ordenada[1:]:
        if (caracter == caracter_anterior):
            contador += 1
        else:
            print(f"{caracter_anterior}: {contador}")
            caracter_anterior = caracter
            contador = 1
    print(f"{caracter_anterior}: {contador}")

def exercicio2_conta_caracteres_dicionario(string_passada):

    dicionario = {}

    for caracter in string_passada:
        dicionario[caracter] = dicionario.get(caracter, 0) + 1

    return dicionario
