def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number + 1,step))

def nb_dig(n, d):
    d = str(d)  # 
    count = 0
    for k in range(n + 1):  
        square = str(k * k)  
        count += square.count(d) 
    return count

def remove_url_anchor(url):
    if "#" in url:
        return url[:url.index("#")]
    else: return url

    def capitals(word):
     return [i for i in range(len(word)) if word[i].isupper()]

def small_enough(array, limit):
    for i in array:
        if i > limit: return False
    return True

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
def reverse_letter(s):
    return ''.join([c for c in s if c.isalpha()])[::-1]

def gimme(triplet):
    return triplet.index(sorted(triplet)[1])

def round_to_next5(n):
    return n if n % 5 == 0 else n + (5 - n % 5)


def two_oldest_ages(ages):
    return sorted(ages)[-2:]
