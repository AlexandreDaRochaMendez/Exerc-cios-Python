# Entrada
# A entrada do programa consiste em uma sequência de códigos de produtos com fim marcado pelo número 0.
# Saída
# A saída do programa deve apresentar o relatório da venda.

codigos_int = range(1, 6)
codigo = 'valor inicial'
batatas = 'Não'
qtd_bebidas = int(0)
m = ''
valores = float(0)
d = int(0)
s = int(0)
p = int(0)

# Refrigerante lata     1
# Suco de laranja       2
# Hamburguer simples    3
# Hamburguer duplo      4
# Batatas fritas        5

while codigo in codigos_int or codigo == 'valor inicial':
    codigo = int(input())
    if codigo == 1:
        valores += 5.00
        qtd_bebidas += 1
    if codigo == 2:
        valores += 8.50
        qtd_bebidas += 1
    if codigo == 3:
        valores += 25.80
        s += 1
    if codigo == 4:
        valores += 28.40
        d += 1
    if codigo == 5:
        valores += 15.00
        batatas = 'Sim'

if d > s:
    m = 'Duplo'
if s > d:
    m = 'Simples'
if s == d and s != 0:
    m = 'Empate'
if s == d and s == 0:
    m = 'Nenhum'

p = valores * 0.3

print('- Relatório da Venda -')
print(f'Quantidade de bebidas vendidas: {qtd_bebidas}')
print(f'Valor total: R$ {valores:.2f}')
print(f'Lucro obtido: R$ {p:.2f}')
print(f'Batatas fritas vendidas? {batatas}')
print(f'Hambúrguer mais vendido: {m}')
