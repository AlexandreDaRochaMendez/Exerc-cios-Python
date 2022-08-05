# A entrada é composta por um par de dados: o nome do mês na primeira linha e a sua temperatura média na segunda linha.
# Esse padrão se repete para todos os meses do ano.

v1 = 0
v2 = 0
ml = []
tl = []

while v1 <= 11:
    m = str(input())
    t = float(input())
    ml.append(m)
    tl.append(t)
    v1 += 1

media = sum(tl) / len(tl)
print(f'{media:.2f}')               # Seu programa deve apresentar na primeira linha a média anual.

while v2 <= 11:                     # deve-se exibir todos os meses cujas temperaturas se igualam ou superaram a média.
    if tl[v2] >= media:
        print((ml[v2]), end='')     # Usar formato: NomeDoMês Temperatura
        print(f'{tl[v2]: .2f}')     # A temperatura também deve ser impressa com duas casas decimais.
    v2 += 1
