import random

# Variables globales proporcionadas por la estructura
items = []
n = 0
stack = []

pivot_index = -1
low_bound = -1
high_bound = -1
i = -1  
j = -1  
state = "PUSH_STACK" # Estados: PUSH_STACK, PARTITION_INIT, PARTITION_STEP, PARTITION_SWAP_PIVOT, DONE

def init(vals):
    global items, n, stack, pivot_index, low_bound, high_bound, i, j, state
    items = list(vals)
    n = len(items)
    stack = []
    pivot_index = -1
    low_bound = -1
    high_bound = -1
    i = -1
    j = -1
    state = "PUSH_STACK"
    
    # Inicial: Agregar el rango completo (0 a n-1) a la pila si hay elementos.
    if n > 1:
        stack.append((0, n - 1))

def partition_init_step():
    """Inicializa un nuevo proceso de partición."""
    global low_bound, high_bound, pivot_index, j, i, state
    
    if not stack:
        state = "DONE"
        return {"done": True}
        
    # Obtener el próximo rango a particionar
    low_bound, high_bound = stack.pop()
    
    if low_bound >= high_bound:
        # Rango con 0 o 1 elemento, ya ordenado. Volver a tomar de la pila.
        return partition_init_step()
    
    # Elegir el pivote
    pivot_index = high_bound 
    
    # Inicializar punteros de la partición
    j = low_bound - 1 
    i = low_bound     
    
    state = "PARTITION_STEP"
    return {"low": low_bound, "high": high_bound, "pivot": pivot_index}

def partition_step_micro():
    """Ejecuta un micro-paso del bucle principal de la partición."""
    global i, j, state, items
    
    if i < high_bound:
        a = i
        b = pivot_index # El pivote es items[high_bound]

        if items[i] <= items[high_bound]:
            j += 1
            if i != j:
                # Intercambiar items[i] con items[j]
                items[i], items[j] = items[j], items[i]
                i += 1
                return {"a": a, "b": j, "swap": True}
        
        i += 1
        return {"a": a, "b": b, "swap": False}
        
    else:
        # El bucle de recorrido ha terminado. Es hora de colocar el pivote.
        state = "PARTITION_SWAP_PIVOT"
        return partition_swap_pivot_step()

def partition_swap_pivot_step():
    """Coloca el pivote en su posición final y prepara la pila."""
    global j, high_bound, pivot_index, state, items
    
    pivot_new_index = j + 1
    a = pivot_new_index
    b = high_bound
    
    # Colocar el pivote (items[high_bound]) en su posición final (j+1)
    items[pivot_new_index], items[high_bound] = items[high_bound], items[pivot_new_index]
    
    # Almacenar los subarreglos para la próxima partición (las "llamadas recursivas")
    # Subarreglo izquierdo
    if low_bound < pivot_new_index - 1:
        stack.append((low_bound, pivot_new_index - 1))
        
    # Subarreglo derecho
    if pivot_new_index + 1 < high_bound:
        stack.append((pivot_new_index + 1, high_bound))
        
    # Volver al estado para inicializar la próxima partición
    state = "PUSH_STACK"
    return {"a": a, "b": b, "swap": True, "pivot_final": pivot_new_index}


def step():
    """Implementa UN micro-paso de Quick Sort."""
    global state
    
    if state == "DONE":
        return {"done": True}
        
    elif state == "PUSH_STACK":
        return partition_init_step()
        
    elif state == "PARTITION_STEP":
        return partition_step_micro()

    elif state == "PARTITION_SWAP_PIVOT":
        return partition_init_step()

    return {"done": True}