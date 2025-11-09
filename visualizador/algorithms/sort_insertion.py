# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

#la primera funcion se realiza una sola vez y es para inicializar las variables globales.
def init(vals):
    global items, n, i, j    #variables globales se inicializan para poder usarlas en diferentes funciones sin tener que ponerlas como parametros.
    items = list(vals)
    n = len(items)
    i = 1  # arrancamos en el segundo elemento
    j = None

#Esta funcion es la que hace los tres pasos restantes pero uno a la vez: primero compara, luego avanza y por ultimo termina el ciclo.
def step():
    global items, n, i, j

    # Si ya terminamos, para saber si no nos excedimos del largo de nuestra lista [items]
    if i >= n:
        return {"done": True}

    # Si recién empezamos con un nuevo elemento, luego de comprobar que todavia estamos dentro de lo permitido
    if j is None:
        j = i
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # Comparar e intercambiar si hace falta
    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        j -= 1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # Si no hay más intercambios, avanzar al siguiente elemento
    i += 1
    j = None
    return {"a": i-1, "b": i, "swap": False, "done": False}
