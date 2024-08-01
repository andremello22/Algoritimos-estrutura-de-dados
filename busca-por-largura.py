from collections import deque
def buscaPorLargura(nome):
    grafo_pessoas = dict()
    grafo_pessoas['voce'] = ['lucia', 'ailton', 'cosme']
    grafo_pessoas['lucia'] = ['marta', 'ronaldo']
    grafo_pessoas['ailton'] = ['margareth']
    grafo_pessoas['cosme'] = ['marlom']
    grafo_pessoas['ronaldo'] = []
    grafo_pessoas['marlom'] = []
    grafo_pessoas['margareth'] = []
    grafo_pessoas['marta'] = []
    fila_vendedores = deque(grafo_pessoas[nome])
    verificados = []
    while fila_vendedores:
        pessoa = fila_vendedores.popleft()
        if not pessoa in verificados:
            if pessoaEvendedor(pessoa):
                print(pessoa + ' é um vendedor')
                return True
            else:
                fila_vendedores.extend(grafo_pessoas[pessoa])
                verificados.append(pessoa)
         
    return False

def pessoaEvendedor(nome):
    return nome[-1] == 'm'


buscaPorLargura("voce")