import time
import random

def is_sorted(arr):
    """
    Verifica se arr está ordenado na ordem crescente.
    """

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]: # comeca a decrescer... falso..
            return False

    return True

############################QUICK SORT TESTS#################################################
def partition(arr, low, high):
    pivot = arr[high]

    pivot_index = low
    i = low

    while i < high:
        if arr[i] < pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
        i += 1

    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    return pivot_index

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def analisa_quick_sort_modificado_para_tamanho(n):
    # da 'build' no array
    arr = [random.randint(1, 1000000) for _ in range(n)]

    start_time = 0

    if not is_sorted(arr):
        start_time = time.time()
        if n <= 15:
            insertion_sort(arr)
        else:
            quick_sort(arr, 0, len(arr) - 1)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # convert to milliseconds

    if is_sorted(arr):
        print(f'Tamanho do vetor: {n}')
        print(f'Tempo decorrido: {elapsed_time} ms')
        print()
    
    else:
        print('Ordenacao falhou.')

def analisa_quick_sort_modificado_para_tamanho(n):
    # da 'build' no array
    arr = [random.randint(1, 1000000) for _ in range(n)]

    start_time = 0

    if not is_sorted(arr):
        start_time = time.time()
        if n <= 100:
            insertion_sort(arr)
        else:
            quick_sort(arr, 0, len(arr) - 1)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # convert to milliseconds

    if is_sorted(arr):
        print(f'Tamanho do vetor: {n}')
        print(f'Tempo decorrido: {elapsed_time} ms')
        print()
    
    else:
        print('Ordenacao falhou.') 


############################MERGE SORT TESTS#################################################
def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def analisa_merge_sort_modificado_para_tamanho(n):
    """
    Ao chamar estas funcao, sera criado um vetor de tamanho n
    que sera ordenado usando merge sort e fara a analise de tempo...

    Merge Sort = O(n log n)
    """

    # da 'build' no array
    arr = [random.randint(1, 1000000) for _ in range(n)]

    start_time = 0

    if not is_sorted(arr):
        start_time = time.time()
        if n <= 15:
            insertion_sort(arr)
        else:
            merge_sort(arr)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # convert to milliseconds

    if is_sorted(arr):
        print(f'Tamanho do vetor: {n}')
        print(f'Tempo decorrido: {elapsed_time} ms')
        print()
    
    else:
        print('Ordenacao falhou.')

############################INSERTION SORT TESTS#################################################
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def analisa_insertion_sort_para_tamanho(n):
    """
    Ao chamar estas funcao, sera criado um vetor de tamanho n
    que sera ordenado usando insertion sort e fara a analise de tempo...

    Insertion Sort = O(n²)
    """

    # da 'build' no array
    arr = [random.randint(1, 1000000) for _ in range(n)]

    start_time = 0

    if not is_sorted(arr):
        start_time = time.time()
        insertion_sort(arr)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # convert to milliseconds

    if is_sorted(arr):
        print(f'Tamanho do vetor: {n}')
        print(f'Tempo decorrido: {elapsed_time} ms')
        print()
    
    else:
        print('Ordenacao falhou.')
