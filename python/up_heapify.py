def up_heapify(L, i):
    def rec(L, i):
        if L[parent(i)] > L[i] and i > 0:
            (L[parent(i)], L[i]) = (L[i], L[parent(i)])
            rec(L, parent(i))
        else:
            return L
    rec(L, i)

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

