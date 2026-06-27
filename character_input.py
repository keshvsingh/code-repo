from datetime import date

user = input("What is your name? ")
age = int(input("What is your age? "))

current_year = date.today().year
to_hundred_year = current_year - age + 100
print(f" {user}, Nice to meet you!!")
print(f"You will be 100 year old in {to_hundred_year} .")