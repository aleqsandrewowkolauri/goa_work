def xor(a,b):
    return a!=b

def get_real_floor(n):
    if n < 1:
        return n
    elif n < 13:
        return n-1
    elif n > 13:
        return n-2

def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if bird not in geese]


def name_shuffler(s):
    parts = s.split()
    return f"{parts[1]} {parts[0]}"

def divisible_by(numbers, divisor):
    return list(filter(lambda x: x%divisor == 0, numbers))

def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))

def plural(n):
    return n == 0 or n > 1

def check_alive(health):
    if health > 0:
        return True
    else:
        return False

def add_five(num):
    total = num + 5
    return total

def combat(health, damage):
    if health - damage > 0: return health - damage
    return 

def how_many_light_sabers_do_you_own(*args):
    if len(args) == 0: return 0
    return 18 if args[0] == "Zach" else 0

def distinct(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

def distinct(arr):
    return list(dict.fromkeys(arr))


def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result

def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result