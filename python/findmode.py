from operator import itemgetter

def mode(L):
    elems = {}
    for i in range(len(L)):
        if L[i] not in elems:
            elems.update({L[i]: 1})
        else:
            elems[L[i]] += 1
    
    maxNum = 0
    maxKey = 0
    for i in range(len(L)):
        if elems[L[i]] > maxNum:
            maxNum = elems[L[i]]
            maxKey = L[i]
    return maxKey
