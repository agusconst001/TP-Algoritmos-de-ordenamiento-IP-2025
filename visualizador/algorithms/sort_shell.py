# ShellSort con micro-pasos para visualización
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
gaps = []       # Lista de gaps (Knuth)
gap_idx = 0     # Índice del gap actual
gap = 0         # Valor del gap actual
i = 0           # Índice principal
j = 0           # Cursor para inserción con gap


def _generate_gaps(size):
    """Genera la secuencia de Knuth: 1, 4, 13, 40, ..."""
    h = 1
    seq = []
    while h < size:
        seq.append(h)
        h = 3 * h + 1
    return seq[::-1]   # Orden descendente


def init(vals):
    global items, n, gaps, gap_idx, gap, i, j
    items = list(vals)
    n = len(items)

    if n <= 1:
        gaps = []
        gap_idx = 0
        gap = 0
        i = j = n
        return

    # Generar gaps
    gaps = _generate_gaps(n)
    if not gaps:
        gaps = [1]

    # Preparar estado inicial
    gap_idx = 0
    gap = gaps[gap_idx]
    i = gap
    j = 0


def step():
    global items, n, gaps, gap_idx, gap, i, j

    # 1) Ver si ya terminamos
    if gap_idx >= len(gaps):
        return {"done": True}

    # 2) Si terminamos la pasada del gap actual → pasar al siguiente
    if i >= n:
        gap_idx += 1

        if gap_idx >= len(gaps):
            return {"done": True}

        gap = gaps[gap_idx]
        i = gap
        j = 0

        # Indicar cambio de gap
        return {"a": i, "b": i - gap, "swap": False, "done": False}

    # 3) Inicializar j si es la primera vez para este i
    if j == 0:
        j = i

    # 4) Comparación y posible swap (mini-paso)
    if j >= gap and items[j - gap] > items[j]:
        a = j - gap
        b = j

        # swap
        items[a], items[b] = items[b], items[a]

        j -= gap
        return {"a": a, "b": b, "swap": True, "done": False}

    # 5) Inserción terminada para items[i]
    i += 1
    j = 0

    if i < n:
        return {"a": i, "b": i - gap, "swap": False, "done": False}

    # Dejar que la siguiente llamada a step() avance al siguiente gap
    return {"done": False}
