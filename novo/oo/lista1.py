# Implementação básica da clássica lista FIFO - First in, First out !

class No:

    def __init__(self, v):
        self.valor = v
        self.proximo_no = None

    # Getters

    @property
    def valor(self):
        return self._valor

    @property
    def proximo_no(self):
        return self._proximo_no

    # Setters

    @valor.setter
    def valor(self, value):
        self._valor = value

    @proximo_no.setter
    def proximo_no(self, value):
        self._proximo_no = value


class Lista:

    def __init__(self):
        self.qtd_nos = 0
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    vetor_impressao = []

    # Getters

    @property
    def qtd_nos(self):
        return self._qtd_nos

    @property
    def primeiro(self):
        return self._primeiro

    @property
    def ultimo(self):
        return self._ultimo

    @property
    def atual(self):
        return self._atual

    # Setters

    @qtd_nos.setter
    def qtd_nos(self, value):
        self._qtd_nos = value

    @primeiro.setter
    def primeiro(self, value):
        self._primeiro = value

    @ultimo.setter
    def ultimo(self, value):
        self._ultimo = value

    @atual.setter
    def atual(self, value):
        self._atual = value

    # Métodos

    def inserir_no(self, novo_no):
        if self.qtd_nos == 0:
            self.primeiro = novo_no
            self.ultimo = novo_no
            self.atual = novo_no
            self.qtd_nos = 1
            print(f'Nó com o valor {novo_no.valor} foi inserido na lista!')
        else:
            self.ultimo.proximo_no = novo_no
            self.ultimo = novo_no
            self.qtd_nos += 1
            print(f'Nó com o valor {novo_no.valor} foi inserido na lista!')

    def remover_no(self):
        if self.qtd_nos == 0:
            print('Lista já está vazia!')
        else:
            self.atual = self.primeiro
            self.primeiro = self.primeiro.proximo_no
            self.atual.proximo_no = None
            print(f'A fila andou!\nNó com o valor {self.atual.valor} foi removido da lista!')
            self.atual = self.primeiro
            self.qtd_nos -= 1

    def print_lista(self):
        if self.qtd_nos == 0:
            print('Lista vazia!')
        else:
            self.vetor_impressao.append(self.atual.valor)
            if self.atual.proximo_no is not None:
                self.atual = self.atual.proximo_no
                self.print_lista()
            else:
                self.atual = self.primeiro
                self.vetor_impressao.sort(reverse=True)
                print(self.vetor_impressao)
                self.vetor_impressao = []
