# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []     
n = 0          # Total de elementos de la lista 'items'.
i = 0          # Contador de pasadas: Indica cuántos elementos ya están ordenados
j = 0          # Contador de comparaciones: Indica el índice del primer elemento del par (j, j+1) a comparar.

def init(vals):
    global items, n, i, j
    items = list(vals)  
    n = len(items)      
    i = 0               # Inicializa el contador de pasadas a 0 (comenzamos la primera pasada).
    j = 0               # Inicializa el índice de comparación a 0 (comenzamos desde el primer numero de la lista).


def step():
    global items, n, i, j     # Declaración de variables globales que serán modificadas.

    # Cuando no queden pasos, devolvé {"done": True}.
    # Chequea si ya termino el algoritmo.
    if i >= n - 1 or n <= 1:
        return {"done": True}

    # 1) Elegir índices a y b a comparar en este micro-paso: j y j+1.
    a = j         # Índice actual
    b = j + 1     # Índice siguiente
    swap = False     # Inicializa la bandera de intercambio en False.

    # Verifica si el índice 'b' está dentro de los límites de la pasada actual (n - i).
    if b < n - i:
        # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
        # Comparación: ¿el elemento 'a' es mayor que el elemento 'b'?
        if items[a] > items[b]:
            # Intercambio
            items[a], items[b] = items[b], items[a]
            swap = True        #Avisa que hubo un intercambio
            
        # 3) Avanzar punteros (preparar el próximo paso).
        # Se incrementa 'j' para pasar al siguiente par de elementos en la próxima llamada a step().
        j += 1
        
        # Pregunta si 'j' ha llegado al final de la parte no ordenada de la lista.
        # Si 'j' llega al final de la pasada, reiniciar 'j' y avanzar 'i'.
        if j >= n - 1 - i:
            i += 1
            j = 0

    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    # Informa al visualizador qué elementos se miraron y si se movieron.
    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False       
    }


