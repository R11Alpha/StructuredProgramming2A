import sys

if __name__ == '__main__':

    x = float(sys.argv[1])
    y = float(sys.argv[2])

    sum = x + y
    minus = x -y
    mult = x * y
    div = x / y

    print("The sum is: {}".format(sum))
    print("The rest is: {}".format(minus))
    print("The multplication is: {}".format(mult))
    print("The division is: {}".format(div))