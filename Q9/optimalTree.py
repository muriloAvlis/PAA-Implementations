import numpy as np
class Node(object):
    def __init__(self, data) -> None:
        '''
        Inicializa a árvore com um nó raiz sem filhos contendo somente a sua chave
        '''
        self.left = None
        self.right = None
        self.key = data

    def insert(self, key) -> None:
        '''
        Insere um nó/chave na árvore a partir da raiz
        '''
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    # def remove(self, root, key) -> None:
    #     '''
    #     Remove um nó/chave na árvore a partir da raiz
    #     '''
    #     if self.key == key and (self.key.right == None and self.key.left == None):

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def deci(tamanho,list_k, lista_kProb, lista_d,lista_dProb):
    soma = 0
    t= 0
    for i in range(0,len(lista_kProb)):
        z = max(lista_kProb)
        x = lista_kProb.index(z)
        #print(lista_kProb)
        t = t+1
        if t <=2:
            soma = soma + z
            print(lista_kProb)
        if t>=3:
            tamanho = 2
            lista_aux = [i * tamanho for i in lista_kProb]
            soma = soma + max(lista_aux)
            print(lista_aux)
        if t>=4:
            tamanho = 3
            lista_aux = [i * tamanho for i in lista_kProb]
            soma = soma + max(lista_aux)
            print(lista_aux)
        lista_aux =[]
        root.insert(list_k[x])
        list_k.remove(list_k[x])
        lista_kProb.remove(z)
        print(soma)
        #print(lista_kProb)
        
    print("fim dos K")
    tamanho = 2
    t = 0
    for i in range(0,len(lista_dProb)):

        z = max(lista_dProb)
        x = lista_dProb.index(z)
        #print(lista_dProb)
        t =t +1
        if t<=3:
            tamanho = 2
            lista_aux = [i * tamanho for i in lista_dProb]
            soma = soma + max(lista_aux)
            print(lista_aux)
        if t>3:
            tamanho =3
            lista_aux = [i * tamanho for i in lista_dProb]
            soma = soma + max(lista_aux)
            print(lista_aux)
        lista_aux =[]
        root.insert(lista_d[x])
        lista_d.remove(lista_d[x])
        lista_dProb.remove(z)
        print(soma)
        #print(lista_dProb)
        
    print("fim dos D")
    soma = soma+1
    return soma
# root
tamanho = 0
root = Node("20")
list_k = ["10","30","40","50"]
lista_kProb = [0.15,0.05,0.10,0.20]
lista_d = ["1","11","22","33","44","55"]
lista_dProb =[0.05,0.1,0.05,0.05,0.05,0.1]
soma = deci(tamanho, list_k, lista_kProb, lista_d,lista_dProb)
print (soma)
root.display()
