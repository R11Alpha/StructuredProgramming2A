hour = float(input("How many hours are you worked?\n"))
extra = 0
salary = 0
if hour > 40:
    extra = (hour - 40) * 1.5
    salary = hour + extra
    print("Your salary is: {}".format(salary))
else:
    print("You're paid")