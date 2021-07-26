import sys
x = len(sys.argv)
sum = 0
for i in range(1, x):
    sum += int(sys.argv[i])

x = x-1
Prom = sum/x

print("\nResult: {}".format(Prom))