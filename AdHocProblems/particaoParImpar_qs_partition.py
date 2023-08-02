def original_qs_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

##########################################

def eh_par(n):
    return n % 2  == 0

def sao_dois_iguais(a, b):
    # True, se a e b tem a mesma 'paridade?'

    if eh_par(a) and eh_par(b):
        return True
    elif not eh_par(a) and not eh_par(b):
        return True

    return False # um eh par outro eh impar


def partition_oddEven_problem(arr, low, high):
    # O(n)

    pivot = arr[high]
    i = low - 1 # i == pointer to last item of the block

    for j in range(low, high):
        if sao_dois_iguais(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

