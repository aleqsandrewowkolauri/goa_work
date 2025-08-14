def row_sum_odd_numbers(n):
    return n ** 3

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

def number(bus_stops):
    people_on_bus = 0
    for on, off in bus_stops:
        people_on_bus += on
        people_on_bus -= off
    return people_on_bus


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

def min_max(lst):
    return [min(lst), max(lst)]

