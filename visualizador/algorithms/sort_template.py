# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0

# Estado del algoritmo (Bubble Sort)
i = 0   # pasada actual
j = 0   # índice dentro de la pasada


def init(vals):
    global items, n, i, j
    items = list(vals)      # copiamos la lista
    n = len(items)          # cantidad de elementos
    i = 0                   # reiniciamos pasada
    j = 0                   # reiniciamos índice


def step():
    global items, n, i, j

    # Si terminamos todas las pasadas → done
    if i >= n - 1:
        return {"done": True}

    # Comparación actual
    a = j
    b = j + 1

    # ¿Hay swap?
    swap = False
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos punteros
    j += 1
    if j >= n - 1 - i:
        j = 0
        i += 1

    # Devolver el micro-paso
    return {"a": a, "b": b,"swap": swap,  "done": False}
            
