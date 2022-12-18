# Cálculo da função hash dos valores a serem inseridos na tabela

# define A
A = ((5**(1/2) - 1) / 2)
# define m | tamanho da tabela
m = 1000

# k == 61
k = 61
# h(k)
h = m * ((k * A) % 1)
print(f'h(61) = {h}')

# k == 62
k = 62
h = m * ((k * A) % 1)
print(f'h(62) = {h}')

# k == 63
k = 63
h = m * ((k * A) % 1)
print(f'h(63) = {h}')

# k == 64
k = 64
h = m * ((k * A) % 1)
print(f'h(64) = {h}')

# k == 65
k = 65
h = m * ((k * A) % 1)
print(f'h(65) = {h}')
