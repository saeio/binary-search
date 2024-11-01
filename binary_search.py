def binary_search(lst, target):
    first= 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first+last)//2

        if lst[midpoint] == target:
            return lst[midpoint]
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print(f"target found at: {index}")
    else: print("Target not found in list")

lista = [1,2,3,4,5,6,7,8,9,20,22]
result = binary_search(sorted(lista), 22)
verify(result)
lista = [1,45,7,8,5,3,6,8,4,3,7,8,5,9,5,8,3465,26,7547,234,883,57,23]
result = binary_search(sorted(lista), 22)
verify(result)
result = binary_search(sorted(lista), 8)
verify(result)
