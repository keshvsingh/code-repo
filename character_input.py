from datetime import date

name = input("What is your Name? ")
age = int(input("What is your age? "))

current_year = date.today().year

hundred_year = current_year - age + 100
print(f"you will be 100 years old in the year {hundred_year}.")

