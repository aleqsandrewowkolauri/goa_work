#davaleba1
def capitalize(s):
    even = [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))  ]
    odd = [s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s))  ]
    return ["".join(even),"".join(odd)]

#davaleba2
def no_odds(values):
    res = []

    for i in values:
        if i%2 == 0:
            res.append(i)

    return res

#davaleba3
def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr2[i] == arr1[i]:
            score += 4
        else: score-= 1
    if score < 0:
        return 0
    return score

#davaleba4
def solve(s):
    lower_count = sum(1 for c in s if c.islower())
    upper_count = len(s) - lower_count  # total - lowercase = uppercase
    return s.lower() if lower_count >= upper_count else s.upper()

#davaleba5
def digits(n):
        return len(str(n))
