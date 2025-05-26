1
def past(h, m, s):
    return h*3600000+m*60000+s*1000

def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"

2
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list

3
def smash(words):
    return " ".join(words)

4
def grow(arr):
    product = 1

    for i in arr:
        product = i

    return product

5
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False

6
def minimum(arr):
    return min(arr)

7
def maximum(arr):
    return max(arr)

8
def fake_bin(x):
    final=""
    for i in x:
        if int(i) < 5:
            final+="0"
        else: final+="1"
    return final

9
def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

10
def county(x, n):
    result = []

    for i in range(1, n+1):
        result.append(x*i)

    return result










