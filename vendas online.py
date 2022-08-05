aceitaveis = [1, 2, 3]
c, n, q, p = 0, 0, 0, 0
vt, t = int(0), int(0)
c_lista = []
n_lista = []
q_lista = []
p_lista = []
lg_lista = []
codigo = 1

codigo = int(input())
while codigo in aceitaveis:
    if codigo == 1:                                         # Um produto a ser cadastrado contem:
        cadastro = input()
        c, n, q, p = cadastro.split(', ')
        c, n, q, p = int(c), str(n), int(q), float(p)
        c_lista.append(c)                                   # um código de identificação (ID);
        n_lista.append(n)                                   # um nome;
        q_lista.append(q)                                   # uma quantidade;
        p_lista.append(p)                                   # e um valor.

    if codigo == 2:                                         # Uma venda contém:
        venda = input()
        c, q = venda.split(', ')
        c, q = int(c), int(q)                               # o ID do produto e uma quantidade.
        try:                                                # Deve haver quantidade suficiente em estoque...
            c = c_lista.index(c)                                # ...,caso isso não ocorra, a venda é ignorada.
            qa = q_lista[c] - q
            if qa == 0:                                     # Caso a quantidade de um produto chegue a zero...
                vt += p_lista[c] * q                            # ..., este deve ser removido do cadastro.
                vi = p_lista[c] * q
                print(f'VALOR DA COMPRA: R$ {vi:.2f}')
                c_lista.pop(c)
                n_lista.pop(c)
                q_lista.pop(c)
                p_lista.pop(c)
            elif qa > 0:                                    # Quando uma venda é efetuada:
                q_lista[c] = qa                             # A quantidade requisitada é descontada...
                vt += p_lista[c] * q                            # ...da quantidade em estoque;
                vi = p_lista[c] * q
                print(f'VALOR DA COMPRA: R$ {vi:.2f}')      # o valor total da compra é exibido.
        except:
            pass

    if codigo == 3:                         # lista
        while t < len(c_lista):
            print(f'ID: {c_lista[t]}, NOME: {n_lista[t]}, QUANTIDADE: {q_lista[t]}, VALOR: {p_lista[t]:.2f}')
            t += 1
    t = 0
    codigo = int(input())

if codigo == 0:
    print(f'TOTAL VENDIDO: R$ {vt:.2f}')
