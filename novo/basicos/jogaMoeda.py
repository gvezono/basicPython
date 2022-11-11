import random

class Moeda:

    def __init__(self):
        self.faces = ['cara','coroa']

    def lancar(self):
        aux = random.randint(0, 1)
        if aux > 0.5:
            return self.faces[1]
        else:
            return self.faces[0]

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def realizar_jogo(self, moeda):
        cara = 0
        coroa = 0
        for i in range(5):
            aux = moeda.lancar()
            if aux == 'cara':
                cara += 1
            else:
                coroa += 1
        if cara > coroa:
            return 'Cara ganhou !'
        else:
            return 'Coroa ganhou!'

if __name__ == '__main__':
    g = Pessoa('Gabriel')
    m = Moeda()
    print(g.realizar_jogo(m))