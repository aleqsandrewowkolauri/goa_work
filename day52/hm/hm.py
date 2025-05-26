#davaleba1
def sum_str(a, b):
    if len(a) > 0 and len(b) == 0: return a
    elif len(a) == 0 and len(b) > 0: return b
    elif len(a) == 0 and len(b) == 0: return "0"

    return str(int(a) + int(b))

#davaleba2
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None  # Handles empty list and single-element list

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    return None  # All elements are consecutive







