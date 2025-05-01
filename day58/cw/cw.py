reverse_and_capitalize = lambda s: s[::-1].capitalize()

print(reverse_and_capitalize("hello"))      
print(reverse_and_capitalize("world"))      
print(reverse_and_capitalize("python"))     





numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]

print(list(map(lambda x: x ** 2, numbers)))