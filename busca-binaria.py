def buscaBinaria(lista, item):
    inicio = 0  # inicio da lista recebe 0
    fim = len(lista) - 1  # fim da lista recebe o tamanho total da lista - 1

    while inicio <= fim:  # enquanto inicio for menor ou igual ao fim, o loop continua
        meio = (inicio + fim) // 2  # meio recebe o inicio da lista mais o fim dividido por dois (divisão inteira)
        chute = lista[meio]  # chute do resultado recebe o meio da lista

        if item == chute:  # se o chute for igual ao item, retorne o índice do meio
            return f'Item {item} encontrado no índice {meio}.'
        if chute > item:  # se o chute for maior que o item da busca, fim recebe meio - 1
            fim = meio - 1
        else:  # caso o chute seja menor que o item, inicio da lista recebe meio + 1
            inicio = meio + 1

    return f'Item {item} não encontrado na lista.'

# Exemplo de uso
lista = [1, 2, 3, 6, 7, 8, 9, 12, 15, 50]

print(buscaBinaria(lista, 50)) 
print(buscaBinaria(lista, -1))  