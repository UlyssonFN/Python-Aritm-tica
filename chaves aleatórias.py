import random
import string

def gerar_chave_delphi():
    # Formato típico: 5 blocos de 5 caracteres (alfanuméricos)
    blocos = []
    for _ in range(5):
        bloco = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        blocos.append(bloco)
    chave = '-'.join(blocos)
    return chave

# Exemplo de uso
for _ in range(5):
    print(gerar_chave_delphi())