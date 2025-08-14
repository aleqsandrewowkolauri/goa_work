def row_sum_odd_numbers(n):
    start_num = 1
    res = []

    for i in range(1, n+1):
        ls = []
        for x in range(i):
            ls.append(start_num)
            start_num += 2
        res.append(sum(ls))

    return res[-1]


def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

def min_max(lst):
    return [min(lst), max(lst)]
