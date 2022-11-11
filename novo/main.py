# Imports
from oo import lista1 as l

# Main
if __name__ == '__main__':

    l1 = l.Lista()

    n1 = l.No('A')
    n2 = l.No('B')
    n3 = l.No('C')

    l1.inserir_no(n1)
    l1.inserir_no(n2)
    l1.inserir_no(n3)

    l1.print_lista()

    l1.remover_no()

    l1.print_lista()

    l1.remover_no()
    l1.remover_no()
    l1.print_lista()
    l1.remover_no()