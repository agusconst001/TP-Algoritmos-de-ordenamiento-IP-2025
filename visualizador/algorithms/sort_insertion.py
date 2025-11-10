# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # Índice del elemento que queremos insertar (desde 1 hasta n-1)
j = None   # Cursor de desplazamiento hacia la izquierda

def init(vals):
    """Inicializa el estado del Insertion Sort."""
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1       
    j = None

def step():
    """Ejecuta un único micro-paso del Insertion Sort."""
    global items, n, i, j

    # 1. Chequeo de finalización
    if i >= n:
        return {"done": True}

    # 2. Inicio del desplazamiento para items[i]
    if j is None:
        # j empieza en la posición de i
        j = i 

        # Si j > 0, devolvemos el primer highlight (comparación con el elemento anterior).
        if j > 0:
            return {"a": j, "b": j - 1, "swap": False, "done": False}
        else:
             # Si i=0 (solo ocurre en listas de 1 elemento) o ya está en posición, avanzar a la siguiente i.
             i += 1
             return step() # Llamar step() de nuevo para verificar el nuevo i o terminar.
    
    # 3. Desplazamiento y Swap Adyacente
    # Condición de swap: j no ha llegado al inicio Y el elemento anterior es mayor que el actual.
    if j > 0 and items[j - 1] > items[j]:
        a = j - 1
        b = j
        
        # Realizar el intercambio
        items[a], items[b] = items[b], items[a]
        
        # Mover el cursor a la izquierda para la siguiente comparación
        j -= 1
        
        return {"a": a, "b": b, "swap": True, "done": False}

    # 4. Finalización de la inserción
    # Si llegamos aquí, el elemento en j ya está en su lugar correcto (j=0 o items[j-1] <= items[j]).
    
    # Avanzar al siguiente elemento a insertar
    i += 1
    
    # Resetear el puntero de desplazamiento
    j = None 
    
    # Devolvemos un paso que resalta el nuevo i si existe, o terminamos.
    if i < n:
        # Resaltamos el nuevo elemento 'i' y su predecesor (i-1) para iniciar la nueva pasada.
        return {"a": i, "b": i - 1, "swap": False, "done": False}
    else:
        return {"done": True}