fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Display the list
print("Here's a list of fruits:", fruits)


try:
    index = int(input("Enter the index of the fruit you want to access (0 to 4): "))
    
  
    print("You selected:", fruits[index])

except IndexError:
    print("Oops! That index is out of range. Please choose a number between 0 and 4.")

except ValueError:
    print("Invalid input! Please enter a number.")