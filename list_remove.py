def remove_duplicate(list):
    dup = []
    for item in list:
        if item not in dup:
            dup.append(item)
    return dup

def remove_duplicate_using_set(input_list):
    new_list = set(input_list)
    
    return list(new_list)

digit = [1, 3, 4, 4, 6, 6, 8, 1]
new_list = remove_duplicate(digit)
print(new_list)
set_list = remove_duplicate_using_set(digit)
print(set_list)