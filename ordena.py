

def partition(lista, start, end):

    pivot = lista[end]
    bottom = start - 1
    top = end

    done = 0

    while not done:
        while not done:
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break

            if lista[bottom] > pivot:
                lista[top] = lista[bottom]
                break

        while not done:
            top = top - 1
            if top == bottom:
                done = 1
                break

            if lista[top] < pivot:
                lista[bottom] = lista[top]
                break

    lista[top] = pivot
    return top


def quick_sort(lista, start, end):
    if start < end:
        split = partition(lista, start, end)
        quick_sort(lista, start, split - 1)
        quick_sort(lista, split+1, end)
    else:
        return


def selection_sort(lista):
    for cont in range(len(lista)):
        index = cont
        for cont2 in range(cont+1, len(lista)):
            if lista[cont2] < lista[index]:
                index = cont2
        if index != cont:
            aux = lista[index]
            lista[index] = lista[cont]
            lista[cont] = aux

    return lista


def insertion_sort(lista):
    for cont in range(1, len(lista)):
        chave = lista[cont]

        aux = cont-1
        while (aux > -1) and chave < lista[aux]:
            lista[aux+1] = lista[aux]
            aux = aux-1
        lista[aux+1] = chave

    return lista


def bubble(lista):
    flag = True
    while (flag):
        flag = False
        for cont in range(0, len(lista)-1):
            if lista[cont] > lista[cont+1]:
                aux = lista[cont]
                lista[cont] = lista[cont+1]
                lista[cont+1] = aux
                flag = True
    return lista