import random
import time
start_time = time.time()        # To know the running time of this program

# Implementação de 'merge sort' em python

def merge_sort(a):
    def merge(a):
        if len(a) > 1:
            m = len(a)//2
            E = a[:m]
            D = a[m:]

            merge(D)
            merge(E)

            i = j = k = 0

            while i < len(E) and j < len(D):
                if E[i] < D[j]:
                    a[k] = E[i]
                    i += 1
                else:
                    a[k] = D[j]
                    j += 1
                k += 1

            while i < len(E):
                a[k] = E[i]
                i += 1
                k += 1

            while j < len(D):
                a[k] = D[j]
                j += 1
                k += 1
        return a
    a = merge(a)
    return a




a = [random.randint(0, 100000) for i in range(10000)]

print(a)
print(merge_sort(a))
print(f"The running time of this program is {round(time.time() - start_time, 5)} seconds.")
# The running time of this program is 0.15571 seconds.

