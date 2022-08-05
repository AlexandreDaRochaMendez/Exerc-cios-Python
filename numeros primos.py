# Identificador de números primos.
# Basta inserir um valor inteiro positivo para saber se ele é primo.
# Para reduzir tempo de processamento são feitas etapas anteriores aos testes por caso.

from math import sqrt
lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
lista_de_divisores = []
primo = False
flag = False

print('Determine um valor positivo para saber se ele é primo.')
x = int(input())

if x < 0:
    print('Por convenção só existem numeros primos positivos')
    exit()
if x in lista:
    print('Sim, primo jà listado.')
    exit()
if x == 0:
    print('zero possui infinitos divisores')
    exit()
if x == 1:
    print('1 não é considerado primo')
    exit()

sq = float(sqrt(x))
if float.is_integer(sq):
    print('Não, possui raiz quadrada')
    flag = True
elif x % 2 == 0:
    print('Não, é par.')
    flag = True
elif x == x:
    for pri in lista:
        c = x % pri
        if c == 0:
            print('Não, possui divisores inteiros.')
            flag = True
            break

if not flag:
    print('')
    print('Fazendo testes.')

    vi = 15
    while x % vi != 0 and x >= 15 and x > vi:
        if x % vi == 0:
            primo = False
            break
        elif vi == x - 2:
            primo = True
            break
        vi = vi + 2

if primo:
    print('Sim, é um número primo.')
    exit()

if not primo and not flag:
    print('Não, possui divisores inteiros.')

print('Deseja ler a lista de divisores?')
resposta = input('s/n -> ')
vs = 1
if resposta == 's':
    print('')
    print(f'criando lista de divisores de \t>{x}<')
    while x != vs:
        if x % vs == 0:
            lista_de_divisores.append(vs)
        vs += 1

lista_de_divisores.append(x)
print(lista_de_divisores)
if resposta == 'n':
    exit('fim')
