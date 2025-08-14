#davaleba1
def in_asc_order(arr):
    if len(arr) <= 1:
        return True
    
    # Compare each element with the next one
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

#davaleba2
def flatten_and_sort(array):
  # Flatten the 2D list using a list comprehension
    flattened = [num for sublist in array for num in sublist]
    
    # Sort and return
    return sorted(flattened)


# Example

#davaleba3
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    # Get the lengths of strings in each array
    lengths1 = [len(s) for s in a1]
    lengths2 = [len(s) for s in a2]

    # The maximum possible difference is between the max of one and the min of the other
    diff1 = max(lengths1) - min(lengths2)
    diff2 = max(lengths2) - min(lengths1)

    return max(diff1, diff2)

#davaleba4
def factorial(n):      
    if n < 0:
        raise ValueError("Negative input not allowed")
    return 1 if n == 0 else n * factorial(n - 1)

# Examples:
def factorial(n):      
    if n < 0:
        raise ValueError("Negative input not allowed")
    return 1 if n == 0 else n * factorial(n - 1)

# Examples:
# factorial(5) -> 120
# factorial(0) -> 1