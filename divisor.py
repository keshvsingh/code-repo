user = int(input("Enter a number? "))
for divisor in range(1,user):

    if user%divisor == 0:
        print(divisor)