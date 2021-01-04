perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'A': '5',
            'B': '3',
            'C': '4',
            'D': '8'
        },
        'resposta_certa': 'C'
    }, 
    'Pergunta 2' : {
        'pergunta': 'Quanto é 8 / 2 ?',
        'respostas': {
            'A': '4',
            'B': '6',
            'C': '5',
            'D': '8'
        },
        'resposta_certa': 'A'
    },
    'Pergunta 3' : {
        'pergunta': 'Quanto é 8 * 2 ?',
        'respostas': {
            'A': '10',
            'B': '20',
            'C': '14',
            'D': '16'
        },
        'resposta_certa': 'D'
    },
}

acertos = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta = input('R:').upper()

    if resposta == pv['resposta_certa']:
        acertos = acertos + 1
        print('Acertou')
    else:
        print('Errou')
    print()

print(f'Você acertou {acertos} resposta(s).')