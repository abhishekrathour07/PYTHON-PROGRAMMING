# country = input("Which country do you live in?")
# print("I live in {0}".format(country))
# a,b=10,20
# print("The values of a is {0} and b is {1}".format(a, b))
# print("The values of b is {1} and a is {0}".format(b,a ))

number_of_days = int(input("Enter number of days"))
number_of_years = int(number_of_days/365)
number_of_weeks = int(number_of_days % 365 / 7)
remaining_number_of_days = int(number_of_days % 365 % 7)
print(f"Years = {number_of_years}, Weeks = {number_of_weeks}, Days = {remaining_number_of_days}")

