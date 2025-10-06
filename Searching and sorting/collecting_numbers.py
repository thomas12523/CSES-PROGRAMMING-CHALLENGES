def selection_sort(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def multiplication(m1,m2):
    res=[[0 for i in range(len(m1))] for i in range(len(m2))]
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1[0])):
                res[i][j]+=m1[i][k]*m2[k][j]
    return res

