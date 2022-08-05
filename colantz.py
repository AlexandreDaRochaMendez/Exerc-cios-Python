try:
    x = int(input())
except:
    print('Entrada inválida')                   # Caso um valor de entrada inválido seja fornecido...
else:                                               # ...seu programa deve acusar uma mensagem de erro.
    if x > 1:
        print('Conjectura de Collatz para N =', x)
        while x != 1:
            if x % 2 == 0:                      # Se o termo anterior for par:
                x = int(x / 2)                  # o próximo termo da sequência será a metade do anterior (N/2).
                x = int(x)
                print(f'{x}\t'+x*'#')           # Para cada número da sequência, imprima a sua quantidade em ‘#’.
            elif x % 2 != 0:                    # Caso o termo anterior seja ímpar:
                x = int(x * 3 + 1)              # o próximo será 3 vezes o termo anterior mais 1 (3N+1).
                print(f'{x}\t'+x*'#')
            else:                               # O número deve ser inteiro positivo.
                print('Entrada inválida')
    else:
        print('Entrada inválida')
