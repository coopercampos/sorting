import random
import time

start_time = time.time()

def selectionSort(a):
    # primeiro começamos com o primeiro item do array, e verificando se ele é menor que o restante 
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[j], a[i] = a[i], a[j]

    return a

a = [random.randint(0, 100000) for i in range(10000)]
print(a)
print(selectionSort(a))
print(f"The running time of this program is {round(time.time()-start_time, 5)} seconds.")
# The running time of this program is 5.65415 seconds.
# This is way more time than the merge sort method with the same array.