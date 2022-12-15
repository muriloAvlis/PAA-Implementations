# by Murilo Silva and Rafael Veiga

# None == espaço vazio ou nunca utilizado (disponível)
# -1 == espaço deletado (D) ou já utilizado (disponível)

class HashTable(object):
    def __init__(self, table: dict = None, m: int = 7) -> None:
        # dimensão da tabela
        self.m = m

        # verifica se a tabela foi repassada
        if table != None:
            self.table = table
        else:
            self.table = self.create_table(self.m)

    def create_table(self, m: int) -> dict:
        return {key: None for key in range(m)}

    def get_hash(self, k: int) -> int:
        return k % self.m

    def get_hash2(self, k: int) -> complex:
        return (1 + (k % 5))

    def insert(self, k: int) -> int:
        h = self.get_hash(k)
        h2 = self.get_hash2(k)
        j = 1
        while h in self.table.keys():
            if self.table[h] == None or self.table[h] == -1:  # não houve colisão
                print(f'Adicionando chave {k} no endereço {h}...')
                self.table[h] = k
                return self.table
            print(f'{j}ª colisão ao inserir {k} (endereço {h} já ocupado!)')
            h = (h + (j*h2)) % self.m  # houve colisão
            j += 1  # incrementa j para o próximo endereço

    def delete(self, k: int) -> int:
        h = self.get_hash(k)
        h2 = self.get_hash2(k)
        j = 1
        while h in self.table.keys() and self.table[h] != None:
            if self.table[h] == k:  # encontrou o valor a ser deletado
                print(f'Removendo chave {k} no endereço {h}...')
                # -1 para D ou deletado / diferenciar de None
                self.table[h] = -1
                return self.table
            print(f'Procurando no próximo endereço...')
            h = (h + (j*h2)) % self.m  # houve colisão
            j += 1  # incrementa j para o próximo endereço


# dimensão da tabela no axis 0 (linhas)
m = 7

# cria a tabela com a dimensão passada
T = HashTable(m=7)
print(f'Tabela criada com tamanho {m}: \n{T.table}\n')

# OPERAÇÕES DE INSERÇÃO

# insere chave 74
T.insert(74)
print(f'{T.table}\n')
# insere chave 92
T.insert(92)
print(f'{T.table}\n')
# insere chave 32
T.insert(32)
print(f'{T.table}\n')
# insere chave 70
T.insert(70)
print(f'{T.table}\n')
# insere chave 47
T.insert(47)
print(f'{T.table}\n')
# Deleta 32
T.delete(32)
print(f'{T.table}\n')
# Insere 49
T.insert(49)
print(f'{T.table}')
