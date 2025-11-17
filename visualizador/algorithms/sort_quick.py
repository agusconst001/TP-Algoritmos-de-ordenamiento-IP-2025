items = []
stack = []
n = 0

# Variables de partición
low_bound = -1
high_bound = -1
pivot_index = -1
i = -1
j = -1

# Estados posibles:
#   PUSH_STACK → tomar un nuevo rango
#   PARTITION_STEP → recorrer y comparar contra el pivote
#   PARTITION_SWAP_PIVOT → colocar el pivote en su posición final
#   DONE → finalizado
state = "PUSH_STACK"


def init(vals):
    global items, n, stack, state
    items = list(vals)
    n = len(items)
    stack = []
    state = "PUSH_STACK"

    if n > 1:
        stack.append((0, n - 1))


def partition_init_step():
    global low_bound, high_bound, pivot_index, i, j, state, stack

    if not stack:
        state = "DONE"
        return {"done": True}

    low_bound, high_bound = stack.pop()

    if low_bound >= high_bound:
        return partition_init_step()

    pivot_index = high_bound
    j = low_bound - 1
    i = low_bound

    state = "PARTITION_STEP"
    return {"low": low_bound, "high": high_bound, "pivot": pivot_index}


def partition_step_micro():
    global i, j, items, high_bound, pivot_index, state

    if i < high_bound:
        a = i
        b = pivot_index

        if items[i] <= items[high_bound]:
            j += 1
            if i != j:
                items[i], items[j] = items[j], items[i]
                i += 1
                return {"a": a, "b": j, "swap": True}

        i += 1
        return {"a": a, "b": b, "swap": False}

    state = "PARTITION_SWAP_PIVOT"
    return partition_swap_pivot_step()


def partition_swap_pivot_step():
    global items, j, high_bound, low_bound, state, stack

    pivot_new_index = j + 1
    a = pivot_new_index
    b = high_bound

    items[pivot_new_index], items[high_bound] = items[high_bound], items[pivot_new_index]

    if low_bound < pivot_new_index - 1:
        stack.append((low_bound, pivot_new_index - 1))

    if pivot_new_index + 1 < high_bound:
        stack.append((pivot_new_index + 1, high_bound))

    state = "PUSH_STACK"
    return {"a": a, "b": b, "swap": True, "pivot_final": pivot_new_index}


def step():
    global state

    if state == "DONE":
        return {"done": True}

    if state == "PUSH_STACK":
        return partition_init_step()

    if state == "PARTITION_STEP":
        return partition_step_micro()

    if state == "PARTITION_SWAP_PIVOT":
        return partition_swap_pivot_step()

    return {"done": True}
