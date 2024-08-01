grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2

print(grafo['inicio'].keys())  

print(grafo["inicio"]["a"])  
print(grafo["inicio"]["b"]) 

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo['fim'] = {}

#################################
infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

###############################

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

###############################
processados = []
###############################

def acheNoCustoMaisBaixo(custos):
    menor_custo = infinito
    nodo_menor_custo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < menor_custo and nodo not in processados:
            menor_custo = custo
            nodo_menor_custo = nodo
    return nodo_menor_custo

nodo = acheNoCustoMaisBaixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = acheNoCustoMaisBaixo(custos)

# Imprime os custos finais e os pais
print("Custos:", custos)
print("Pais:", pais)

