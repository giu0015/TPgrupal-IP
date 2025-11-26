# Quick_Sort 

items = []
stack = []          # Pila con (left, right)
i = j = pivot = None
current_left = current_right = None
state = None
done = False


def init(vals):
    global items, stack, i, j, pivot, state, done
    global current_left, current_right

    items = list(vals)
    stack = [(0, len(items) - 1)]   # Segmento inicial
    i = j = pivot = None
    current_left = current_right = None
    state = None
    done = False


def step():
    global items, stack, i, j, pivot, state, done
    global current_left, current_right

    # Si ya terminó todo
    if done:
        return {"done": True}

    # Si no quedan segmentos, se debe terminar
    if not stack and state is None:
        done = True
        return {"done": True}

    # Inicio de nuevo segmento
    if state is None:
        current_left, current_right = stack.pop()
        pivot = items[current_right]
        i = current_left - 1
        j = current_left
        state = "partition"
        return {"a": current_right, "b": j, "swap": False, "done": False}

    # Fase de partición
    if state == "partition":

        # Mientras j no llegó al pivote
        if j < current_right:

            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                j += 1
                return {"a": i, "b": j-1, "swap": True, "done": False}

            else:
                j += 1
                return {"a": j-1, "b": None, "swap": False, "done": False}

        # Si j llegó al final, se debe colocar el pivote
        items[i+1], items[current_right] = items[current_right], items[i+1]
        piv_idx = i + 1

        # Agregar subsegmentos
        if piv_idx - 1 > current_left:
            stack.append((current_left, piv_idx - 1))

        if piv_idx + 1 < current_right:
            stack.append((piv_idx + 1, current_right))

        # Prepararse para el siguiente segmento
        state = None
        return {"a": piv_idx, "b": current_right, "swap": True, "done": False}
