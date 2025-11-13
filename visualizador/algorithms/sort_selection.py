# Contrato: init(vals), step() -> {"a": int|None, "b": int|None, "swap": bool, "done": bool}

items = []
n = 0
i = 0          
j = 0          
min_idx = 0    
fase = "buscar"  # Puede ser "buscar" o "swap"

def init(vals):
    """Inicializa el estado del algoritmo Selection Sort paso a paso."""
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0


    if n <= 1:
        return {"a": None, "b": None, "swap": False, "done": True}

    j = i + 1
    min_idx = i
    fase = "buscar"

    return {"a": i, "b": j, "swap": False, "done": False}


def step():
    """Ejecuta un paso del algoritmo Selection Sort."""
    global items, n, i, j, min_idx, fase

    # --- 1. Chequeo de finalización ---
    if i >= n - 1:
        return {"a": None, "b": None, "swap": False, "done": True}

    # --- 2. FASE DE BÚSQUEDA ---
    if fase == "buscar":
        if j < n:
            j_actual = j

            # Comparar items[j] con items[min_idx]
            if items[j] < items[min_idx]:
                min_idx = j  # Nuevo mínimo encontrado

            # Avanzar el cursor
            j += 1

            # Devolver el paso actual de comparación
            return {"a": min_idx, "b": j_actual, "swap": False, "done": False}

        else:
            # Se terminó el barrido → pasar a la fase de swap
            fase = "swap"
            return step()  # Ejecutar inmediatamente la fase de swap

    # --- 3. FASE DE SWAP ---
    elif fase == "swap":
        a = i
        b = min_idx
        realizado_swap = False

        # Si el mínimo no está donde debería, intercambiamos
        if i != min_idx:
            items[a], items[b] = items[b], items[a]
            realizado_swap = True

        # Preparar el estado para la siguiente iteración
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"

        # Devolver el resultado del intercambio
        return {"a": a, "b": b, "swap": realizado_swap, "done": False}

    # Si llega aquí, algo inesperado ocurrió
    return {"a": None, "b": None, "swap": False, "done": True}
