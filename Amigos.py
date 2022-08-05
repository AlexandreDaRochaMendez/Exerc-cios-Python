# Dizemos que dois números são considerados ‘amigos’ quando cada um deles é igual à soma dos divisores próprios do outro

n1 = int(input())                                                       # A entrada consiste em duas linhas...
n2 = int(input())                                                           # ...representando os dois números inteiros.
lista_n1 = []
lista_n2 = []
i = int(1)
j = int(1)

lista_n1.append(int(1))
lista_n2.append(int(1))
while n1 / i > 1:
    i += 1
    if i < n1:
        if n1 % i == 0:
            lista_n1.append(i)
        if i == n1 - 1:
            break

while n2 / j > 1:
    j += 1
    if j < n2:
        if n2 % j == 0:
            lista_n2.append(j)
        if j == n2 - 1:
            break

# ' '.join(map(str, LISTA)
# para valores int

sn1 = sum(lista_n1)
sn2 = sum(lista_n2)
lista_n1m = ' '.join(map(str, lista_n1))
lista_n2m = ' '.join(map(str, lista_n2))

print(f'Divisores próprios de {n1}: {lista_n1m} cuja soma é {sn1}')     #A saída é composta pela lista de divisores...
print(f'Divisores próprios de {n2}: {lista_n2m} cuja soma é {sn2}')         # ...em seguida a soma dos divisores

if sn1 == n2 and sn2 == n1:                                             # Uma mensagem indicando se são amigos.
    print(f'{n1} e {n2} são amigos')
else:
    print(f'{n1} e {n2} não são amigos')
