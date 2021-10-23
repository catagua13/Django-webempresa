import random
aleatorio = random.randint(0, 100)
if aleatorio == 0:
    print(f'LLego a {aleatorio}')
else:
    while aleatorio !=0:
        aleatorio = random.randint(0, 10)
        aleatorio = aleatorio
        lista = aleatorio
        cont = 0
        for i in range(2, lista + 1):
            primos = True
            for j in range(2, 11):
                if i == j:
                    break
                elif i % j == 0:
                    primos = False
                else:
                    continue
            if primos == True:
                print(' ', i, end='')
                cont += 1
        print('\nHay %u números primos.' % cont)


