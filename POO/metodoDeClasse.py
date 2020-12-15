from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Metodo da classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    

    # Metodo estatico
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand



p1 = Pessoa('Eduardo', 25)
print(p1.idade)
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('Eduardo2', 1995)
print(p2.idade)
p2.get_ano_nascimento()

print(Pessoa.gera_id())