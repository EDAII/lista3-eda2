from ordena import quick_sort
import random


lista = []

print("Escolha uma opção de vetor")
print("1 - Aleatorio")
print("2 - Inverso Ordenado")
opc = input()

if(opc == '1'):
    for cont in range(0, 100):
        lista.append(random.randint(0, 20))
elif(opc == '2'):
    lista = list(range(100, 0, -1))


print("Escolha uma opção de ordenação")
print("1 - Quick Sort")

opc = input()

if(opc == '1'):
    quick_sort(lista, 0, len(lista)-1)    
    print(lista)


