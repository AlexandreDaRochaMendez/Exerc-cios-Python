# Entrada
# Uma string representando uma sequência de DNA (com potenciais carecteres inválidos).
# Saída
# A sequência complementar dos caracteres válidos, apenas.

dna = input()
t = 0

while t < len(dna):
    letra = dna[t]
    t += 1
    if letra == 'A':
        print('T', end = '')
    elif letra == 'T':
        print('A', end = '')
    elif letra == 'C':
        print('G', end = '')
    elif letra == 'G':
        print('C', end = '')
    else:
        pass
print()