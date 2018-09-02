#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from ordena import quick_sort, bubble, insertion_sort, selection_sort
from sortTimer import SortTimer
import random


lista = []

print("Escolha uma opção de vetor")
print("1 - Aleatorio")
print("2 - Inverso Ordenado")
print("3 - Ordenado")
opc = input()

if(opc == '1'):
    lista = random.sample(range(100), 100)
elif(opc == '2'):
    lista = list(range(100, 0, -1))
elif(opc == '3'):
    lista = list(range(0, 100))


timer = SortTimer(lista)

data_bubble = timer.get_time_taken(bubble)
data_insertion = timer.get_time_taken(insertion_sort)
data_selection = timer.get_time_taken(selection_sort)
data_quick = timer.get_time_taken(quick_sort, True)

plt.plot(data_bubble["n_of_elements"], data_bubble["time_taken"],
         label='bublle')

plt.plot(data_insertion["n_of_elements"], data_insertion["time_taken"],
         label='insertion')

plt.plot(data_selection["n_of_elements"], data_selection["time_taken"],
         label='selection')

plt.plot(data_quick["n_of_elements"], data_quick["time_taken"], label='quick')
plt.legend()
plt.show()
