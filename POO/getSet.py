class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setter
    @preco.setter 
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('RS', ''))
        self._preco = valor

    @nome.setter
    def nome(self, text):
        self._nome = text.title()



p1 = Produto('CAMISA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 15)
p2.desconto(10)
print(p2.nome, p2.preco)