# QuickSort con registro completo de pasos para visualización

items = [64, 25, 12, 22, 11]  # lista inicial
steps = []  # aquí guardaremos cada paso como dict {"a", "b", "swap", "items"}

def quicksort(arr, low, high):
    if low < high:
        # dividir
        pi = partition(arr, low, high)
        # ordenar recursivamente izquierda y derecha
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        # registrar la comparación
        steps.append({
            "a": j,
            "b": high,
            "swap": False,
            "items": arr.copy()
        })
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            # registrar el swap
            steps.append({
                "a": i,
                "b": j,
                "swap": True,
                "items": arr.copy()
            })
            i += 1
    # swap del pivote
    arr[i], arr[high] = arr[high], arr[i]
    steps.append({
        "a": i,
        "b": high,
        "swap": True,
        "items": arr.copy()
    })
    return i

# ejecutar QuickSort
quicksort(items, 0, len(items) - 1)

# mostrar resultado final
print("Lista ordenada:", items)
print("\nPasos para visualización:")
for s in steps:
    print(s)

