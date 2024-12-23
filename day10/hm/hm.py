# დავალება 1
weight = float(input("გთხოვთ, მიუთითოთ თქვენი წონა (კილოგრამებში): "))
height = float(input("გთხოვთ, მიუთითოთ თქვენი სიმაღლე (მეტრებში): "))
bmi = weight / (height ** 2)
print(f"თქვენი BMI არის: {bmi:.2f}")

# დავალება 2
a = 10
b = 5
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# დავალება 3
a = 5
b = -12
c = 1000
d = 0
e = 7
f = -56
g = 230
h = 99999
i = -320
j = 45

a = "Hello"
b = "Python"
c = "12345"
d = "True"
e = "John Doe"
f = "2024"
g = "abc"
h = "Hello, World!"
i = "10.5"
j = "Happy Day"

a = 3.14
b = -2.5
c = 100.0
d = 0.0
e = 9.8
f = -56.78
g = 1200.5
h = 0.9
i = -4.56
j = 0.001

str_value = "123"
int_value = int(str_value)
float_value = float(str_value)

# დავალება 4
a = 10
b = 5
print(f"{a} > {b}: {a > b}")
c = 3
d = 7
print(f"{c} > {d}: {c > d}")
a = 10
b = 5
print(f"{a} < {b}: {a < b}")
c = 3
d = 7
print(f"{c} < {d}: {c < d}")
a = 10
b = 5
print(f"{a} >= {b}: {a >= b}")
a = 3
b = 3
print(f"{a} >= {b}: {a >= b}")
a = 10
b = 5
print(f"{a} <= {b}: {a <= b}")
a = 7
b = 8
print(f"{a} <= {b}: {a <= b}")
a = 10
b = 10
print(f"{a} == {b}: {a == b}")
a = 10
b = 5
print(f"{a} != {b}: {a != b}")

# დავალება 5
age = int(input("გთხოვთ, მიუთითოთ თქვენი ასაკი: "))
print(f"10 წელში თქვენ იქნებით {age + 10} წლის")

# დავალება 6
age1 = int(input("მომხმარებელი 1 - თქვენი ასაკი: "))
age2 = int(input("მომხმარებელი 2 - თქვენი ასაკი: "))
age3 = int(input("მომხმარებელი 3 - თქვენი ასაკი: "))
average_age = (age1 + age2 + age3) / 3
print(f"მოსაწვდომი სამი ადამიანის საშუალო ასაკი არის: {average_age:.2f}")

# დავალება 7
number1 = float(input("გთხოვთ, მიუთითოთ პირველი რიცხვი: "))
number2 = float(input("გთხოვთ, მიუთითოთ მეორე რიცხვი: "))

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2
division_first = number1 // number2
division_second = number2 // number1

print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference_result}")
print(f"ნამრავლი: {product_result}")
print(f"განაყოფი: {quotient_result}")
print(f"პირველი რიცხვის ხარისხად მეორე რიცხვი: {division_first}")
print(f"მეორე რიცხვის ხარისხად პირველი რიცხვი: {division_second}")

# დავალება 8
number1 = float(input("გთხოვთ, მიუთითოთ პირველი რიცხვი: "))
number2 = float(input("გთხოვთ, მიუთითოთ მეორე რიცხვი: "))
number3 = float(input("გთხოვთ, მიუთითოთ მესამე რიცხვი: "))

sum_result = number1 + number2 + number3
difference_result = number1 - number2 - number3
product_result = number1 * number2 * number3
quotient_result = number1 / number2 / number3

print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference_result}")
print(f"ნამრავლი: {product_result}")
print(f"განაყოფი: {quotient_result}")
 