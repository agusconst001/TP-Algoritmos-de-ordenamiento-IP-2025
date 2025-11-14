# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0 #cantidad de elementos
i = 0 #pasada actual
j = 0  #indice que recorre y compara elementos

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items) 
    i = 0
    j = 0
    
    if n <= 1: #si la lista tiene 0 o 1 elemento, ya está ordenada
        i = n 


def step():
    global items, n, i, j
    #-------- evalua si i ha llegado al final de la lista
    if i >= n - 1:
        return {"done": True}
    
    #--------- se definen dos indices a y b para comparar
    a = j 
    b = j + 1 
    swap = False  #indica si se hizo un intercambio
    
    max_j = n - i - 1 ############
    
    #-------- compara e intercambia si es necesario
    if a < max_j:
        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
            
        # Avanzar el puntero j para la siguiente comparación
        j += 1
        
        return {"a": a, "b": b, "swap": swap, "done": False}
    ###################################
    else:
        i += 1
        j = 0
        
        if i >= n - 1:
            return {"done": True}
        else:
            return {"a": 0, "b": 1, "swap": False, "done": False}
    