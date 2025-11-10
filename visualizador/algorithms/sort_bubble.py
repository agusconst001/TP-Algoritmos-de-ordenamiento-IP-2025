# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

# Variables globales para mantener el estado del algoritmo
items = []
n = 0
i = 0  # Indica el número de elementos ya ordenados al final
j = 0  # Índice actual de la burbuja (comparando j con j+1)

def init(vals):
    """Inicializa el estado del algoritmo."""
    global items, n, i, j
    items = list(vals)  # 1) Guardar copia
    n = len(items)      # 2) Guardar n
    i = 0               # 3) Inicializar punteros
    j = 0
    # Si la lista está vacía o tiene un solo elemento, ya está ordenada.
    if n <= 1:
        i = n

def step():
    """Ejecuta un único micro-paso del Bubble Sort."""
    global items, n, i, j
    
    # --- 1. Verificar si ha terminado ---
    # La lista está ordenada cuando i alcanza n-1 (o n, si manejamos el caso n<=1 en init)
    if i >= n - 1:
        return {"done": True}

    # --- 2. Definir índices a comparar ---
    a = j
    b = j + 1
    swap = False
    
    # El rango de comparación en esta pasada (definido por i) es hasta el índice n - i - 1
    max_j = n - i - 1 

    # --- 3. Realizar comparación y posible intercambio ---
    if a < max_j:
        # Se compara items[j] con items[j+1]
        if items[a] > items[b]:
            # Realizar el intercambio (swap)
            items[a], items[b] = items[b], items[a]
            swap = True
        
        # Avanzar el puntero j para la siguiente comparación
        j += 1
        
        # --- 4. Devolver el resultado del micro-paso ---
        return {"a": a, "b": b, "swap": swap, "done": False}

    # --- 5. Fin de la pasada (j alcanzó el final del segmento no ordenado) ---
    else: # j == max_j
        # Reiniciar j a 0 y avanzar i (un elemento más ha quedado ordenado al final)
        i += 1
        j = 0
        
        # En el último paso de una pasada, solo avanzamos i y j. 
        # La UI necesita una comparación para mostrar, pero para ser estrictos con un micro-paso,
        # podríamos devolver el estado de i y j como indicadores del fin del loop interno.
        # Simplificamos: devolvemos los índices del final de la pasada anterior.
        # Si i >= n - 1 después de incrementar, hemos terminado.
        if i >= n - 1:
             return {"done": True}
        
        # Devolvemos una "no-operación" para indicar el fin de la pasada
        # Usamos los nuevos índices de inicio de la siguiente pasada.
        return {"a": 0, "b": 1, "swap": False, "done": False} # Se podría refinar la devolución aquí.