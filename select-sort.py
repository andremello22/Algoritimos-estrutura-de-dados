def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def selectionSort(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


arr = [10,29,1,3,9,5,11,0,1,]
print(selectionSort(arr))