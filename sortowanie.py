import numpy as np
import time


A = np.random.randint(5,size=5000)
zmiana=1
zakres = len(A)-1
start = time.time()
while zakres > 0 and zmiana:
       zmiana = False
       for i in range(zakres):
           if A[i]>A[i+1]:
               zmiana = True
               buf = A[i]
               A[i] = A[i+1]
               A[i+1] = buf
       zakres -= 1
end = time.time()
print("czas babelkowy:",end - start)

B = np.random.randint(5, size=5000)
startB = time.time()
for licz in range(len(B)-1,0,-1):
       pierwszy=0
       for ten in range(1,licz+1):
           if B[ten]>B[pierwszy]:
               pierwszy = ten

       bufB = B[licz]
       B[licz] = B[pierwszy]
       B[pierwszy] = bufB
endB = time.time()
print("czas selection sort:",endB - startB)

C = np.random.randint(5, size=5000)
def quicksort(tablica):
    lewa = []
    equal = []
    prawa = []

    if len(tablica) > 1:
        pivot = tablica[0]
        for liczba in tablica:
            if liczba < pivot:
                lewa.append(liczba)
            elif liczba == pivot:
                equal.append(liczba)
            elif liczba > pivot:
                prawa.append(liczba)
        return quicksort(lewa)+equal+quicksort(prawa)
    else:
        return tablica


startC = time.time()
D = quicksort(C)
endC = time.time()
print(D)
print("czas quicksort:",endC - startC)
