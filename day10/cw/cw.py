# დავალება 1: შექმენით 3 ცვლადი, თითოეულში შეინახეთ მომხმარებლის შემოტანილი რიცხვი
number1 = float(input("გთხოვთ, მიუთითოთ პირველი რიცხვი: "))
number2 = float(input("გთხოვთ, მიუთითოთ მეორე რიცხვი: "))
number3 = float(input("გთხოვთ, მიუთითოთ მესამე რიცხვი: "))

# დაბეჭდეთ ეს სამივე ცვლადი
print(f"პირველი რიცხვი: {number1}")
print(f"მეორე რიცხვი: {number2}")
print(f"მესამე რიცხვი: {number3}")


#davaleba 2
weight = float(input("გთხოვთ, მიუთითოთ თქვენი წონა (კილოგრამებში): "))
height = float(input("გთხოვთ, მიუთითოთ თქვენი სიმაღლე (მეტრებში): "))
bmi = weight / (height ** 2)
print(f"თქვენი BMI არის: {bmi:.2f}")

a = 10
b = 5
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
