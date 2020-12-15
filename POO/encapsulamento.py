# public metodos e atributos que podem ser acessados de qualquer lugar 
# protected podem ser acessados apenas dentro da classe, ou dos filhos dessa classe
# private so pode ser acessado dentro da classe

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

bd = BaseDeDados()
bd.inserir_cliente(1, 'Eduardo')
bd.inserir_cliente(2, 'Mario')
bd.inserir_cliente(3, 'Fernanda')

print(bd.dados)