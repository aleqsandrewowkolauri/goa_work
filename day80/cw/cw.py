#davaleba1
def number_lines(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]

#davaleba2
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
