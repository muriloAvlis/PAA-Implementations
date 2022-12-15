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

    def removeABB(self, root, key) -> object:
        '''
        Remove um nó/chave na árvore a partir da raiz
        '''
        # Raiz não passada ou não encontrada
        if root is None:
            print(f'Valor não {key} encontrado na árvore!')
            return root

        # chave menor que a raiz, então varre subárvore da esquerda
        if key < root.key:
            root.left = self.removeABB(root.left, key)

        # chave maior que a raiz, então varre subárvore da direita
        elif key > root.key:
            root.right = self.removeABB(root.right, key)

        # chave igual a raiz, elemento a ser removido encontrado
        else:
            # caso em que a raiz possui apenas um nó filho
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp

            # caso a raiz possua dois nós filhos
            # acha o menor valor à direita
            tmp = self.minValueRight(root.right)

            # substitui a chave pelo menor valor à direita
            root.key = tmp.key

            # deleta o valor substituido
            root.right = self.removeABB(root.right, tmp.key)

        return root

    def minValueRight(self, key):
        '''
        Encotrar o menor valor a partir de uma chave
        '''
        while(key.left is not None):
            key = key.left
        return key

    def display(self):
        '''
        Imprime a árvore no terminal
        '''
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        '''
        Retorna a lista de strings, comprimento, altura e coordenada horizontal da raiz
        '''
        # Sem filho
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Apenas filhos à esquerta
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Apenas filhos à direita
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Filhos à esquerda e à direita
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


# root
root = Node(10)
# root.printTree()
root.insert(5)
root.insert(15)
root.insert(20)
root.insert(14)
root.display()
root.removeABB(root, 15)
root.display()
