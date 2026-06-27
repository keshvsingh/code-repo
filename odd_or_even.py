user = int(input("Enter a number :- "))
number = user/4
if user%2==0:
    print("It is even.")
elif user%4 == 0:
    print("Its a even-lucky number.")
else:
    print("It is odd.")

while True:
    check = int(input("Enter a even number :- "))
    divide_check = check%2
    if divide_check == 0:
        print("you absolutely written even number.")
        break
    else:
        print("Try again!")
