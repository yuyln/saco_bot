import numpy as np
with open("adjetivos.txt", "r", encoding='UTF-8') as arq2:
    adjetivos = arq2.read().split("\n")
    adj_return = []
    for adjetivo in adjetivos:
        if adjetivo.endswith('s'):
            adjetivo = ''.join(list(adjetivo)[:-1])
        if adjetivo.endswith('a'):
            adjetivo = list(adjetivo)
            adjetivo[-1] = 'o'
            adjetivo = ''.join(adjetivo)
        if adjetivo.endswith('ã'):
            adjetivo = list(adjetivo)
            adjetivo[-1] = 'o'
            adjetivo = ''.join(adjetivo)
        if adjetivo.endswith('á'):
            adjetivo = list(adjetivo)
            adjetivo[-1] = 'o'
            adjetivo = ''.join(adjetivo)            
        adj_return.append(adjetivo)
#adj_return = set(adj_return)
#hm = np.unique(adj_return)
hm = set(adj_return.copy())
with open('adjetivos_tratado.txt', 'w', encoding='UTF-8') as arq:
    arq.write(f"{'/'.join(hm)}")
print((hm))
