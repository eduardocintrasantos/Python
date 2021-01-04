"""
função - escopo
"""

variavel = 'global'

def func():
    variavel2 = 'escopo da função'
    print(variavel2)

def func2():
    variavel = 'um novo valor'
    print(variavel)
    global variavel3
    variavel3 = 'variavel global dentro de uma funcao'


print(variavel)
func()
func2()
print(variavel3)