# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0

# Punteros / estado del algoritmo
i = 0         # posición actual a fijar
j = 0         # puntero para buscar mínimo
min_idx = 0   # índice del mínimo actual
fase_busqueda = True  # True = buscando mínimo; False = toca intercambiar

# Métricas (opcionales)
comparaciones = 0
intercambios = 0

def init(vals):
    """
    Inicializa el estado del algoritmo.
    Se llama 1 sola vez al iniciar / remezclar.
    """
    global items, n, i, j, min_idx, fase_busqueda, comparaciones, intercambios
    items = list(vals)   # COPIA obligatoria
    n = len(items)

    # inicializar punteros
    i = 0
    j = i + 1
    min_idx = i
    fase_busqueda = True

    # reiniciar métricas
    comparaciones = 0
    intercambios = 0

def step():
    """
    Realiza UN micro-paso del algoritmo y devuelve el dict requerido:
    {"a": int, "b": int, "swap": bool, "done": bool}
    Cuando termina debe devolver {"done": True}
    """
    global items, n, i, j, min_idx, fase_busqueda, comparaciones, intercambios

    # Si la lista tiene 0 o 1 elementos, ya está ordenada
    if n <= 1:
        return {"done": True}

    # Si ya completamos todas las posiciones
    if i >= n - 1:
        return {"done": True}

    # Fase: buscar el mínimo en items[i..n-1]
    if fase_busqueda:
        # Asegurarnos de que j esté en rango; si no, pasamos a intercambio
        if j >= n:
            fase_busqueda = False
            # No devolvemos indices inválidos aquí; pasamos a la fase de intercambio
            return step()

        # devolver la comparación entre j y min_idx
        a = j
        b = min_idx

        # contabilizar comparación (si índices válidos)
        if 0 <= j < n and 0 <= min_idx < n:
            comparaciones += 1
            if items[j] < items[min_idx]:
                min_idx = j

        # avanzar j para el siguiente micro-paso
        j += 1

        # si j llegó al final, la próxima llamada hará el intercambio
        if j >= n:
            fase_busqueda = False

        return {"a": a, "b": b, "swap": False, "done": False}

    # Fase: intercambio de items[i] con items[min_idx], si corresponde
    else:
        # índices seguros para devolver
        a = i
        b = min_idx

        # Si min_idx es distinto de i, hacemos swap real
        if 0 <= a < n and 0 <= b < n and a != b:
            # swap real en la lista antes de devolver swap=True
            items[a], items[b] = items[b], items[a]
            intercambios += 1

            # Preparar punteros para la siguiente iteración
            i += 1
            j = i + 1
            min_idx = i
            fase_busqueda = True

            return {"a": a, "b": b, "swap": True, "done": False}

        else:
            # Si min_idx == i, no hay intercambio: solo avanzamos
            i += 1
            j = i + 1
            min_idx = i
            fase_busqueda = True

            # devolvemos los índices (aunque swap=False)
            # esto permite que el visualizador destaque la posición fija
            return {"a": a, "b": b, "swap": False, "done": False}
            
