from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if self.comendo == True:
            print(f'{self.nome} não pode falar em quanto come')
        elif self.falando == False:
            print(f'{self.nome} está falando sobre {assunto}')
            self.falando = True
        else:
            print(f'{self.nome} já está falado')
    
    def parar_falar(self):
        if self.falando == False:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        else:
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True

    def parar_comer(self):
        if self.comendo == True:
            print(f'{self.nome} acabou de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo.')
        