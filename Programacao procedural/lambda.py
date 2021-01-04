"""
função anonima
"""

lista = [
    ['P1', 5],
    ['P2', 8],
    ['P3', 50],
    ['P4', 35],
    ['P5', 15],
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
# ou
print(sorted(lista, key=lambda i: i[1], reverse=False))