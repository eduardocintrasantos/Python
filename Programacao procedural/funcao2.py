"""
função - *args  **kwargs
*  utilizado para desempacotamento de argumentos
** é utilizado para argumentos nomeados.. Ex: nome='eduardo'
"""
def func(*args, **kwargs):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')
    if idade is None:
        print('Idade não informada')
    else:
        print(idade)


func(1,2,3,4,5,6)
lista2 = [7,8,9,10,11]
func(1,2,3,4,5,6, *lista2, nome='eduardo', sobrenome='cintra')

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1,n2,n)

print(lista)
print(*lista, sep='-')