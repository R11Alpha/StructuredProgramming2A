print("This is a great program xD\n")

x1 = int(input("Introduce the first number\n"))
x2 = int(input("Introduce the second number\n"))

answer1 = input("Do you want to add?(Yes/No)\n")

if answer1 == "Yes":
    sum = x1 + x2
    print("\nThe sum is {}".format(sum))
else:
    answer2 = input("Do you want to multiply?(Yes/No)\n")
    
    if answer2 == "Yes":
        mul = x1 * x2
        print("\nThe multiplication is {}".format(mul))
    else: 
        print("Goodbye")