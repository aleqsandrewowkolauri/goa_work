#davaleba 1
student_info = {
    "name": "გიორგი",
    "surname": "პეტრაშვილი",
    "academy": "თბილისის სახელმწიფო უნივერსიტეტი",
    "fav-color": "ლურჯი",
    "city": "თბილისი",
    "goa-student": True,
    "age": 21,
    "fav-programming-lang": "Python"
}

for key, value in student_info.items():
    print(f"{key}: {value}")



#davaleba 2
student_info = {
    "name": "John",
    "age": 25,
    "major": "Computer Science",
    "university": "MIT",
    "fav-language": "Python"
}

# 1. Print all the keys in the dictionary using the keys() method
print("Keys in the dictionary:")
print(student_info.keys())

# 2. Print all the values in the dictionary using the values() method
print("\nValues in the dictionary:")
print(student_info.values())

# 3. Print all key-value pairs using the items() method
print("\nKey-Value pairs in the dictionary:")
print(student_info.items())

# 4. Iterate over the dictionary using the items() method and print each key with its corresponding value
print("\nIterating over the dictionary:")
for key, value in student_info.items():
    print(f"{key}: {value}")


