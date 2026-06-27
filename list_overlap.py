a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


common_list = [item for item in a if item in b]
print(common_list)


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [item for item in a if item%2==0]
print(new_list)