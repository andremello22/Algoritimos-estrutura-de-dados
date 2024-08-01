
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0] #ideal é que o pivô seja aleatório
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quickSort(menores) + [pivo] + quickSort(maiores)
    

arr = [90,10,15,20,100,]
print(quickSort(arr))
