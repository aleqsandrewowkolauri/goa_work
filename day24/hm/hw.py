#დავალება 1
#ფუნქცია იმაში გამოიყენება რომ  საშუალებას იძლევა კოდის ორგანიზებას 

#homework 2
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print("First element:", first_element)

#homework 2
last_element = my_list[-1]
print("Last element:", last_element)

#homework 3
first_three_elements = my_list[:3]
print("First three elements:", first_three_elements)

#homework 4
my_string = "HelloWorldPython"
last_five_elements = my_string[-5:]
print("Last five elements:", last_five_elements)

#homework 5
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

# homework 6
every_third_element = my_list[::3]
print("Every third element:", every_third_element)

# homework 7
if len(my_list) % 2 == 0:  # სიის სიგრძე უნდა იყოს ლუწი
    mid_index = len(my_list) // 2
    first_half = my_list[:mid_index]
    second_half = my_list[mid_index:]
    print("First half:", first_half)
    print("Second half:", second_half)
else:
    print("List length is not even, can't split into two equal halves.")