#davaleba1
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

#davaleba2
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))

#davaleba3
def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"

#davaleba4

def filter_list(lst):
    return [x for x in lst if isinstance(x, int) and x >= 0]

#davaleba5



