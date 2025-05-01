starts_with_a = lambda s: s.startswith('A')

print(starts_with_a("Apple"))   
print(starts_with_a("apple"))   

starts_with_a = lambda s: s.lower().startswith('a')