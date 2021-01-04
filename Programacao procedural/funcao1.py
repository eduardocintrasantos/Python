"""
função - def
"""

def funcao(msg='Olá', nome='Mundo'):
    print(f'{msg} {nome}!')

funcao()
funcao('Oi', 'Eduardo')

# -------------

def tabuada(n):
    print(f'-- Tabuada do {n} --')
    for i in range(11):
        print(f'{i} x {n} = {i*n}')

tabuada(5)
tabuada(3)
tabuada(8)
print()
print()

# -------------

def percentual(val, per):
    aumento = val * (per / 100)
    return val + aumento

print(percentual(100, 10))
print()
print()

# -------------

def FizzBuzz(n):
    for i in range (1, n):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} = FizzBuzz')
        elif i % 3 == 0:
            print(f'{i} = fizz')
        elif i % 5 == 0:
            print(f'{i} = buzz')
        else:
            print(i)

FizzBuzz(30)