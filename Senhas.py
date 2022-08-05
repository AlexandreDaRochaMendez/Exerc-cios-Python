# Entrada: Uma string representando a senha.
# Saída: Indicação de se a senha é forte ou fraca.

senha = input()
forca = 0
t = 0

while t < len(senha) - 1:

    if senha[t] == senha[t+1]:                  # Não conter 2 caracteres repetidos em sequência
        forca -= 1
        break
    t += 1

if not any(x.isupper() for x in senha):         # Conter, pelo menos, 1 letra minúscula, 1 maiúscula e 1 dígito
    forca -= 1
if not any(x.islower() for x in senha):
    forca -= 1
if not any(x.isdigit() for x in senha):
    forca -= 1

if len(senha) < 6 or len(senha) > 20:           # Ter pelo menos 6 e no máximo 20 caracteres
    forca -= 1

if forca == 3:
    print('senha forte')
elif forca < 3:
    print('senha fraca')
