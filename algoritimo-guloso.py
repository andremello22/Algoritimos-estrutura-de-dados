estacoes = {
    'Kum': set(["id", "nv", "ut"]),
    'Kdois': set(["wa", "id", "mt"]),
    'Ktres': set(["or", "nv", "ca"]),
    'Kquatro': set(["nv", "ut"]),
    "Kcinco": set(["ca", "az"])
}

def verificaMaiorAreaDeCobertura(estacoes):
    # Conjunto de todos os estados que precisam ser cobertos
    estados_abranger = set()
    for estados in estacoes.values():
        estados_abranger.update(estados)
    
    estacoes_finais = set()
    while estados_abranger:
        melhor_estacao = None
        melhor_cobertura = set()
        
        # Encontrar a estação que cobre o maior número de estados restantes
        for estacao, estados in estacoes.items():
            cobertos = estados_abranger & estados
            if len(cobertos) > len(melhor_cobertura):
                melhor_estacao = estacao
                melhor_cobertura = cobertos
        
        # Remover os estados cobertos pela melhor estação encontrada
        estados_abranger -= melhor_cobertura
        # Adicionar a melhor estação ao conjunto de estações finais
        estacoes_finais.add(melhor_estacao)

    return estacoes_finais



print("Estações finais:", verificaMaiorAreaDeCobertura(estacoes))


