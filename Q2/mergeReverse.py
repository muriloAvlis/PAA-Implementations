'''
Universidade Federal do Pará
Instituto de Ciência Exatas e Naturais
Programa de Pós-Graduação em Ciência da Computação
Projeto e Análise de Algoritmos
Alunos:
- Murilo Cruz da Silva - 202220070016
- Rafael Veiga Teixeira e Silva - 202220070007
'''

# INTERCALAÇÃO E INVERSÃO DE LISTA

# importação de bibliotecas
import numpy as np  # a utilização do numpy é devido a melhor performance
from timeit import timeit  # utilizado para medir o tempo de execução das funções


def merge(l1: list, l2: list) -> list:
    '''
    Retorna uma lista a partir da intercalação dos nós/indexes de duas listas de entrada.

    :param l1: list
    :param l2: list
    :return: list

    Exemplos
    >>> merge([2.1, 4.5, 1.0], [7.2, 9.8])
    array([2.1, 7.2, 4.5, 9.8, 1. ])
    '''
    L = np.array([])  # lista resultante
    idx = 1  # indexes impares p/ l2
    for i in range(0, len(l1)):
        L = np.append(L, l1[i])  # adiciona todos os itens de l1 em L

    for j in range(0, len(l2)):
        # insere todos os itens de l2 nos indexes impares de L ou nos indexes finais caso idx for maior que o último index
        L = np.insert(L, idx, l2[j])
        if idx >= (len(L) - 1):
            idx = len(L)
        else:
            idx += 2
    return L


def reverse(l: list) -> list:
    '''
    Retorna uma lista com os elementos invertidos dado uma lista de entrada.

    :param l: list
    :return: list

    Exemplos
    >>> reverse([2.1, 7.2, 4.5, 9.8, 1. ])
    [1.0, 9.8, 4.5, 7.2, 2.1]
    '''
    return l[::-1]  # np.flip(l) também pode ser utilizado


if __name__ == '__main__':
    lista1 = np.array([2.1, 4.5, 1.0])
    lista2 = np.array([7.2, 9.8])
    print(f'Lista 1: {lista1}')
    print(f'Lista 2: {lista2}')
    L = merge(l1=lista1, l2=lista2)
    print(f'Lista resultante intercalada: {L}')
    L = reverse(L)
    t_merge = timeit('merge(lista1, lista2)', number=1,
                     globals=globals())  # medição do tempo do merge em 1 execução
    t_reverse = timeit('reverse(L)', number=1,
                       globals=globals())  # medição do tempo do reverse em 1 execução
    print(f'Lista invertida: {L}')
    print(f'Tempo de execução do merge: {t_merge} s')
    print(f'Tempo de execução do reverse: {t_reverse} s')
