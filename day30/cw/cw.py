# მომხმარებლის სახელი შემოსატანა
name = input("მიუთითეთ თქვენი სახელი: ")

# მომხმარებლის არჩევანის შემოსატანა
choice = input("შეარჩიეთ 'u' ან 'l': ")

# მასობრივი გადმოტვირთვა მიხედვით
if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("wrong information")