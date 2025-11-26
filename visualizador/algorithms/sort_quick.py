# Quick_Sort paso a paso

items = []
rangos = []          # Pila con (left, right)
i = j = pivot = None
current_izquierda = current_derecha = None
estado = None
done = False


def init(vals):
    global items, rangos, i, j, pivot, estado, done
    global current_izquierda, current_derecha

    items = list(vals)
    rangos = [(0, len(items) - 1)]   # Segmento inicial
    i = j = pivot = None
    current_izquierda = current_derecha = None
    estado = None
    done = False


def step():
    global items, rangos, i, j, pivot, estado, done
    global current_izquierda, current_derecha

    # Si ya terminó todo
    if done:
        return {"done": True}

    # Si no quedan segmentos pendientes
    if not rangos and estado is None:
        done = True
        return {"done": True}

    # Inicio de un nuevo segmento
    if estado is None:
        current_izquierda, current_derecha = rangos.pop()
        pivot = items[current_derecha]
        i = current_izquierda - 1
        j = current_izquierda
        estado = "partition"
        return {"a": current_derecha, "b": j, "swap": False, "done": False}

    # Fase de partición
    if estado == "partition":

        # j todavía no llegó al pivote
        if j < current_derecha:

            # Si el elemento es <= pivote → va al sector menor
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                j += 1
                return {"a": i, "b": j-1, "swap": True, "done": False}

            # Si es > pivote → solo avanzar
            else:
                j += 1
                return {"a": j-1, "b": None, "swap": False, "done": False}

        # Cuando j termina → fijar el pivote en su posición final
        items[i+1], items[current_derecha] = items[current_derecha], items[i+1]
        pos_fija = i + 1

        # Agregar subsegmentos
        if pos_fija - 1 > current_izquierda:
            rangos.append((current_izquierda, pos_fija - 1))

        if pos_fija + 1 < current_derecha:
            rangos.append((pos_fija + 1, current_derecha))

        # Termina partición → próximo segmento
        estado = None
        return {"a": pos_fija, "b": current_derecha, "swap": True, "done": False}
