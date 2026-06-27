a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
    if item<5:
        print(item)
        # new_list.append(item)
    
new_list = [item for item in a if item<5]
print(new_list)

ask_number = input("Enter a number? ")
ask_number = int(ask_number)

ask_list = [item for item in a if item<ask_number]
print(ask_list)