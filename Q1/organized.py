import random
import time
import numpy
arr = []
for i in range(100000):
    r = random.randint(0, 1000000)
    arr.append(r)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while (i < len(left) and j < len(right)):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare=lambda x, y: x < y):
    # Função lambda usada para ordenar um array em ordem crescente e decrescente.
    # Por padrão, ela ordena o array em ordem crescente
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


def quicksort(z):
    if(len(z) > 1):
        piv = int(len(z)/2)
        val = z[piv]
        lft = [i for i in z if i < val]
        mid = [i for i in z if i == val]
        rgt = [i for i in z if i > val]

        res = quicksort(lft)+mid+quicksort(rgt)
        return res
    else:
        return z


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

 # See if left child of root exists and is
 # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

 # See if right child of root exists and is
 # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

 # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

  # Heapify the root.

        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

 # One by one extract elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


def countingSort(inputArray):
    # Find the maximum element in the inputArray
    maxElement = max(inputArray)

    countArrayLength = maxElement+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase
    # the corresponding count for every element by 1
    for el in inputArray:
        countArray[el] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


# Numeros aleatorios
print("para valores 100000")
print("#######################################################################################################################################################################################\n")
print("Valores aleatorios\n")
print("heapsoft 100000\n")
inicio = time.time()
heapSort(arr)
fim = time.time()
print(fim - inicio)

print("MergeSort 100000\n")
inicio = time.time()
merge_sort(arr)
fim = time.time()
print(fim - inicio)

print("QuickSort 100000\n")
inicio = time.time()
ans1 = quicksort(arr)
fim = time.time()
print(fim - inicio)

print("Counting sort 100000\n")
inicio = time.time()
sortedArray = countingSort(arr)
fim = time.time()
print(fim - inicio)


aro = []
for i in range(100000):
    aro.append(i)
print("#######################################################################################################################################################################################\n")
print("Valores em ordem\n")
print("heapsoft 100000\n")
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 100000\n")
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 100000\n")
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 100000\n")
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)

print("#######################################################################################################################################################################################\n")
print("Valores em ordem inversa\n")
print("heapsoft 100000\n")
aro = []
for i in range(100000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 100000\n")
aro = []
for i in range(100000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 100000\n")
aro = []
for i in range(100000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 100000\n")
aro = []
for i in range(100000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)


arr = []
for i in range(10000):
    r = random.randint(0, 10000)
    arr.append(r)
print("#######################################################################################################################################################################################\n")
print("Valores aleatorios\n")
print("heapsoft 10000\n")
inicio = time.time()
heapSort(arr)
fim = time.time()
print(fim - inicio)

print("MergeSort 10000\n")
inicio = time.time()
merge_sort(arr)
fim = time.time()
print(fim - inicio)

print("QuickSort 10000\n")
inicio = time.time()
ans1 = quicksort(arr)
fim = time.time()
print(fim - inicio)

print("Counting sort 10000\n")
inicio = time.time()
sortedArray = countingSort(arr)
fim = time.time()
print(fim - inicio)


aro = []
for i in range(10000):
    aro.append(i)
print("#######################################################################################################################################################################################\n")
print("Valores em ordem\n")
print("heapsoft 10000\n")
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 10000\n")
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 10000\n")
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 10000\n")
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)

print("#######################################################################################################################################################\n")
print("PARA VALORES 10000")
print("Valores em ordem inversa\n")
print("heapsoft 10000\n")
aro = []
for i in range(10000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 10000\n")
aro = []
for i in range(10000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 10000\n")
aro = []
for i in range(10000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 10000\n")
aro = []
for i in range(10000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)


arr = []
for i in range(1000):
    r = random.randint(0, 10000)
    arr.append(r)
print("#######################################################################################################################################################################################\n")
print("Valores aleatorios\n")
print("heapsoft 1000\n")
inicio = time.time()
heapSort(arr)
fim = time.time()
print(fim - inicio)

print("MergeSort 1000\n")
inicio = time.time()
merge_sort(arr)
fim = time.time()
print(fim - inicio)

print("QuickSort 1000\n")
inicio = time.time()
ans1 = quicksort(arr)
fim = time.time()
print(fim - inicio)

print("Counting sort 1000\n")
inicio = time.time()
sortedArray = countingSort(arr)
fim = time.time()
print(fim - inicio)


aro = []
for i in range(1000):
    aro.append(i)
print("#######################################################################################################################################################################################\n")
print("Valores em ordem\n")
print("heapsoft 1000\n")
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 1000\n")
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 1000\n")
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 1000\n")
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)

print("#######################################################################################################################################################\n")
print("PARA VALORES 1000")
print("Valores em ordem inversa\n")
print("heapsoft 1000\n")
aro = []
for i in range(1000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
heapSort(aro)
fim = time.time()
print(fim - inicio)

print("MergeSort 1000\n")
aro = []
for i in range(1000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
merge_sort(aro)
fim = time.time()
print(fim - inicio)

print("QuickSort 1000\n")
aro = []
for i in range(10000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
ans1 = quicksort(aro)
fim = time.time()
print(fim - inicio)

print("Counting sort 1000", end='')
aro = []
for i in range(1000):
    aro.append(i)
aro.sort(reverse=True)
inicio = time.time()
sortedArray = countingSort(aro)
fim = time.time()
print(fim - inicio)
