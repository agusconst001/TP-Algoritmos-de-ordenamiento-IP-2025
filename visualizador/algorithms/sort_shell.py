# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
gaps = []       # Lista de intervalos (p.ej., secuencia de Knuth: 1, 4, 13, 40, ...)
gap_idx = 0     # Índice del 'gap' actual que estamos usando (de mayor a menor)
gap = 0         # Valor del intervalo actual (h = gaps[gap_idx])
i = 0           # Inicio de la sub-lista (de 'gap' a 'n')
j = 0           # Cursor para el Insertion Sort dentro del sub-grupo (j = i - gap)

def _generate_gaps(size):
    """Genera la secuencia de intervalos de Knuth: 1, 4, 13, 40, ..."""
    h = 1
    h_list = []
    # Genera la secuencia mientras h sea menor que n/3
    while h < size // 3:
        h_list.append(h)
        h = 3 * h + 1
    return h_list[::-1] # Devuelve la lista en orden descendente

def init(vals):
    global items, n, gaps, gap_idx, gap, i, j
    items = list(vals)
    n = len(items)
    
    # Si n <= 1, terminamos inmediatamente.
    if n <= 1:
        gaps = []
        gap_idx = 0
        gap = 0
        i = n
        j = n
        return

    # Inicializar punteros/estado
    gaps = _generate_gaps(n)
    gap_idx = 0
    
    # Si la lista de gaps está vacía (n es muy pequeño), forzamos un gap de 1.
    if not gaps:
        gaps = [1] 
    
    gap = gaps[gap_idx]
    i = gap             # El Insertion Sort empieza a evaluar desde el índice 'gap'
    j = 0               # Se inicializa antes de la primera comparación

def step():
    global items, n, gaps, gap_idx, gap, i, j

    # --- 1. Chequeo de finalización ---
    # Terminamos si hemos recorrido todos los gaps (y el último fue 1)
    if gap_idx >= len(gaps):
        return {"done": True}

    # --- 2. Fase de Inserción (Insertion Sort con paso 'gap') ---
    
    # 2a. Si hemos terminado la pasada del gap actual (i >= n), pasamos al siguiente gap.
    if i >= n:
        gap_idx += 1
        
        # Si terminamos todos los gaps, devolver {"done": True}
        if gap_idx >= len(gaps):
            return {"done": True} 
            
        # Pasar al siguiente gap
        gap = gaps[gap_idx]
        i = gap
        j = 0
        
        # Devolver un paso para mostrar que el gap ha cambiado (usamos i y j como indicadores)
        return {"a": i, "b": i - gap, "swap": False, "done": False}

    # 2b. Inicializar o continuar el desplazamiento 'j' (similar a Insertion Sort)
    if j == 0:
        # j es el punto de inicio para el desplazamiento hacia atrás
        j = i
        
    # 2c. Realizar la comparación y potencial swap
    # Condición: j no ha llegado al inicio del sub-grupo (j >= gap) Y están desordenados
    if j >= gap and items[j - gap] > items[j]:
        a = j - gap
        b = j
        
        # Realizar el intercambio (swap)
        items[a], items[b] = items[b], items[a]
        
        # Mover el cursor 'j' hacia atrás por el valor del gap
        j -= gap
        
        # Devolver el paso de swap
        return {"a": a, "b": b, "swap": True, "done": False}

    # 2d. Inserción completada para items[i]
    else:
        # El elemento en 'i' ha sido insertado correctamente
        
        # Avanzar al siguiente elemento a evaluar en la lista principal
        i += 1 
        
        # Reiniciar j para la siguiente inserción (j=0)
        j = 0 
        
        # Devolver el paso de comparación final (resaltamos el elemento que acabamos de insertar y el que le sigue)
        if i < n:
            return {"a": i, "b": i - gap, "swap": False, "done": False}
        else:
            # Si i justo alcanzó 'n', volvemos a llamar para pasar al siguiente gap.
            return step()