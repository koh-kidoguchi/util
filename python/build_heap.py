from up_heapify import up_heapify

def build_heap(L):
    for i in range(len(L)):
        up_heapify(L, i)
    return L