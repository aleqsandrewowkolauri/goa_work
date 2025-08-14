def validate_pin(pin):
    digits = "0123456789"
    for i in pin:
        if i not in digits:
            return False
    return len(pin)==4 or len(pin)==6

def is_triangle(a, b, c):
    return a+b>c and b+c>a and c+a>b


def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))


    def open_or_senior(data):
     res = []

    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")

    return res

def find_next_square(sq):
    
    # შევამოწმოთ თუ არის perfect square
    if int(sq**0.5)*int(sq**0.5) != sq: return -1

    # დავაბრუნოთ შემდეგი perfect square
    return (int(sq**0.5)+1)**2


def solution(string, ending):
    return string.endswith(ending)


def accum(s):
    return '-'.join(char.upper() + char.lower() * i for i, char in enumerate(s))

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

def friend(names):
    return [name for name in names if len(name) == 4]

def maskify(cc):
    return '#' * max(len(cc) - 4, 0) + cc[-4:]

def add_binary(a, b):
    return bin(a + b)[2:]

