# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0 
j = 0 
min_idx = 0
fase = "BUSCANDO" # "BUSCANDO" el mínimo, o "INTERCAMBIANDO"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = 1
    min_idx = 0
    fase = "BUSCANDO"

def step():
    global items, n, i, j, min_idx, fase
    if i >= n:
        return {"done": True}
    if fase == "BUSCANDO":
        if j == i + 1:
            min_idx = i
        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            return {"a": i, "b": j - 1, "min_idx": min_idx, "done": False}
        else:
            fase = "INTERCAMBIANDO"
            return {"a": i, "b": i, "min_idx": min_idx, "done": False}

    elif fase == "INTERCAMBIANDO":
        swap = (i != min_idx)
        
        if swap:
            items[i], items[min_idx] = items[min_idx], items[i]
        i += 1        
        j = i + 1      
        fase = "BUSCANDO" 
        return {"a": i - 1, "b": min_idx, "swap": swap, "done": False}

    return {"done": True}