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
def get_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

#davaleba6
def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)

#davaleba7
def XO(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#davaleba8
def to_jaden_case(s):
    return ' '.join(word.capitalize() for word in s.split())
