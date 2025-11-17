# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0   
j = None   

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1       
    j = None

def step():
    global items, n, i, j
    if i >= n:
        return {"done": True}
    
    if j is None:
        j = i 
        if j > 0:
            return {"a": j, "b": j - 1, "swap": False, "done": False}
        else:
            i += 1 
            return step()
        
    if j > 0 and items[j - 1] > items[j]:
        a = j - 1
        b = j
        # Realizar el intercambio
        items[a], items[b] = items[b], items[a]
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    i += 1
    j = None 
    if i < n:
        return {"a": i, "b": i - 1, "swap": False, "done": False}
    else:
        return {"done": True}