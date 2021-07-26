
minimun = int(input("Enter minimun range limit: "))
maximun = int(input("Enter maximun range limit: "))


for i in range(minimun, maximun + 1):
   if (i%3 == 0) & (i%5 == 0):
      print("{}".format(i))

exit()