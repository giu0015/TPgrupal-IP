# QuickSort — versión paso a paso adaptada al template
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0

# Estado del algoritmo
stack = []      # pila de rangos (low, high)
low = 0
high = 0
pivot = 0
i = 0
j = 0
fase = ""       # "inicio", "comparacion", "pivot_swap"


def init(vals):
    global items, n, stack, fase, low, high, i, j, pivot
    items = list(vals)
    n = len(items)

    # comenzamos con un solo rango: la lista entera
    stack = [(0, n - 1)]

    fase = "inicio"  # siguiente step inicia nueva partición
    low = high = pivot = 0
    i = j = 0


def step():
    global items, n, stack
    global low, high, pivot, i, j, fase

    # Si ya no hay más rangos → terminado
    if not stack:
        return {"done": True}

    # -------------------------------
    # 1) INICIO DE PARTICIÓN
    # -------------------------------
    if fase == "inicio":
        low, high = stack.pop()

        # rangos inválidos o triviales (1 elemento)
        if low >= high:
            fase = "inicio"
            return {"a": low, "b": high, "swap": False, "done": False}

        pivot = items[high]  # elegimos pivote = último elemento

        i = low               # zona para menores
        j = low               # puntero de recorrido

        fase = "comparacion"
        return {"a": j, "b": high, "swap": False, "done": False}

    # -------------------------------
    # 2) COMPARACIÓN Y SWAPS INTERNOS
    # -------------------------------
    if fase == "comparacion":

        # ¿ya terminamos de recorrer?
        if j >= high:
            fase = "pivot_swap"
            return {"a": i, "b": high, "swap": False, "done": False}

        a = j
        b = high
        swap = False

        # comparo con el pivote
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            swap = True
            i += 1

        j += 1

        return {"a": a, "b": b, "swap": swap, "done": False}

    # -------------------------------
    # 3) SWAP FINAL CON EL PIVOTE
    # -------------------------------
    if fase == "pivot_swap":
        items[i], items[high] = items[high], items[i]

        # agregar rangos nuevos para ordenar
        stack.append((low, i - 1))
        stack.append((i + 1, high))

        fase = "inicio"

        return {"a": i, "b": high, "swap": True, "done": False}
