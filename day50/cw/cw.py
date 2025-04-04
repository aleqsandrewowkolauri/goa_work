#davaleba 1
num = 10

try:
   
    result = num + "string"
except TypeError as e:
    print(f"მოხდა TypeError: {e}")


#davaleba 2
try:
    name = input("შეიყვანეთ თქვენი სახელი: ").strip()
    surname = input("შეიყვანეთ თქვენი გვარი: ").strip()

    if not name or not surname:
        raise ValueError("სახელი და გვარი არ შეიძლება იყოს ცარიელი!")

    if not name.isalpha() or not surname.isalpha():
        raise ValueError("სახელი და გვარი უნდა შეიცავდეს მხოლოდ ასოებს!")

    print(f"მოგესალმებით, {name} {surname}!")

except ValueError as ve:
    print(f"მოხდა ValueError: {ve}")
except KeyboardInterrupt:
    print("\nპროცესი შეწყდა მომხმარებლის მიერ.")
except Exception as e:
    print(f"მოხდა გაუთვალისწინებელი შეცდომა: {e}")