#davaleba1
def series_sum(n):
    total = 0
    for i in range(n):
        total += 1 / (1 + 3 * i)
    return f"{total:.2f}"

#davaleba2
def divisors(n):
    result = [i for i in range(2, n) if n % i == 0]
    return result if result else f"{n} is prime"

#davaleba3
def remove_smallest(numbers):
    if not numbers:
        return []

    min_index = numbers.index(min(numbers))
    return numbers[:min_index] + numbers[min_index + 1:]

#davaleba4
def number_lines(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]

#davaleba5
def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

#davaleba6
def stray(arr):
    for num in set(arr):
        if arr.count(num) == 1:
            return num

#davaleba7
def solution(nums):
    if not nums:
        return []
    return sorted(nums)

#davaleba8
def arithmetic(a, b, operator):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]

#davaleba9
def break_chocolate(n, m):
    if n == 0 or m == 0:
        return 0
    return n * m - 1

#davaleba10
def are_anagrams(str1, str2):
    # Convert both strings to lowercase and sort the letters
    return sorted(str1.lower()) == sorted(str2.lower())

