def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]

def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

def find_short(s):
    s=s.split()
    lenghts=[]
    for i in s:
        lenghts.append(len(i))
    return min(lenghts)

def add_binary(a, b):
    return bin(a + b)[2:]



