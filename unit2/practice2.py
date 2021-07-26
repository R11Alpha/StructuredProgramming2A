import sys

if __name__ == "__main__":
    print("Practice 2 CodeBloks")
    edificio = [    [0,1,1,2],
                    [0,5,0,0],
                    [2,0,3,3]]
    
    for i in range(0, len(edificio[0])):
        #print(f" i: {i}, {edificio[i]}")
        for j in range(0, len( edificio)):
            print(f"edificio[{i}][{j}]: {edificio[{j}][{i}]}")
