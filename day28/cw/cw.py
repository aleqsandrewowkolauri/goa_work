classwork 1
def manual_index(main_str, search_str):
    if search_str in main_str:
        return main_str.index(search_str)
    return -1

main_string = "hello world"
search_string = "world"
result = manual_index(main_string, search_string)
print(result)