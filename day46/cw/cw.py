#davaleba 1
def manual_list(start, end, step, user_num):
    result = [num for num in range(start, end, step) if num > user_num]
    return result


print(manual_list(1, 20, 2, 5))   # [7, 9, 11, 13, 15, 17, 19]
print(manual_list(10, 50, 5, 25)) # [30, 35, 40, 45]
print(manual_list(-10, 10, 3, -2)) # [0, 3, 6, 9]




#davaleba 2
filtered_numbers = [num for num in range(1, 101) if (num % 3 == 0) ^ (num % 5 == 0)]
print(filtered_numbers)

#davaleba 3
palindromic_numbers = [num for num in range(10, 201) if str(num) == str(num)[::-1]]
print(palindromic_numbers)
