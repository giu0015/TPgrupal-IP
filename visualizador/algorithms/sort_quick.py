# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
stack = []      # Pila con los rangos pendientes de procesar
i = j = pivot = None
state = None    # Estado interno (partitioning o avanzando)
done = False

def init(vals):
    global items, stack, i, j, pivot, state, done
    items = list(vals)
    stack = [(0, len(items) - 1)]   # Rango inicial completo
    i = j = pivot = None
    state = None
    done = False


def step():
    global items, stack, i, j, pivot, state, done

    if done:
        return {"done": True}

    # Si ya no quedan rangos para ordenar → terminó
    if not stack:
        done = True
        return {"done": True}

    # Si recién empezamos con un nuevo segmento
    if state is None:
        left, right = stack.pop()
        pivot = items[right]        # Elegimos el pivote
        i = left - 1
        j = left
        state = "partition"
        return {"a": right, "b": j, "swap": False, "done": False}

    # Fase de partición
    left, right = None, None
    if state == "partition":
        left, right = 0, 0  # valores dummy

        # Si j todavía no llegó al final del segmento
        if j < right:
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                j += 1
                return {"a": i, "b": j-1, "swap": True, "done": False}
            else:
                j += 1
                return {"a": j-1, "b": None, "swap": False, "done": False}

        # Cuando j termina → colocar el pivote en su lugar
        items[i+1], items[right] = items[right], items[i+1]
        piv_idx = i+1

        # Agregar sub-segmentos a la pila
        if piv_idx - 1 > left:
            stack.append((left, piv_idx - 1))
        if piv_idx + 1 < right:
            stack.append((piv_idx + 1, right))

        state = None    # Reiniciar para el próximo rango
        return {"a": piv_idx, "b": right, "swap": True, "done": False}
