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

    result = 1
    for i in range(2, n+1):
        result *= i

    return result