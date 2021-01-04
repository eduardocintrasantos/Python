def func():
    var = 'variavel'
    return var

def func2(arg):
    print(arg)

variavel = func()
func2(variavel)

# -------------

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

def responde(*args):
    print(args)

responde(fala_oi('eduardo'), saudacao('Olá', 'Eduardo'), 'e')
