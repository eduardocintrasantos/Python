d1 = {'chave1':'valor da chave'}
d1['chave2'] = 'valor da chave2'

print(d1)

d2 = dict(chave1='valor1', chave2='valor2', chave3='valor3')
print(d2)
print(d2['chave2'])

if d2.get('chave3') is not None:
    print(d2.get('chave3'))
else:
    print('Essa chave não existe')

if d2.get('chave4') is not None:
    print(d2.get('chave4'))
else:
    print('Essa chave não existe')

d2['chave1'] = 'Um novo valor'
print(d2['chave1'])

d2.update({'nova_chave':'novo_valor'})
print(d2)
del d2['nova_chave']
print(d2)

print()
print('chave1' in d2)
print('chave1' in d2.keys())
print('valor3' in d2.values())
print(len(d2))

for k in d2:
    print(k)

for v in d2.values():
    print(v)

for k, v in d2.items():
    print(k, v)

print()
copia_d2 = d2.copy()
copia_d2['chave2'] = 'teste'
print(copia_d2)
print(d2)

