import sys, math

tempF= [63, 73, -999, 91, 86, 82, 72, 81, 66, 77, 75, 104, -999, 84, 77, 66, 82, 63, 93, 72, 82, 64, 75 , 90, 64, -999, 99, 82, 95, 82]
tempFN=list(filter(lambda x: x >= 0, tempF))
tempFN.sort()

constante=32
constante2=(5/9)
tempC=[]
tempCF=[]


for i in tempFN:
    tempC.append(i-constante)

for i in tempC:
    tempCF.append(i*constante2)


rounded_tempCF = [ round(elem, 2) for elem in tempCF ]

print("Farenheit temperatures:\n",tempFN)
print("\n")
print ("Celcius temperatures:\n",rounded_tempCF)
print("\n")


def max (values):
    maximum=values[0]

    for i in range(1, len(values)):
        if values[i]>maximum:
            maximum= values[i]
    return maximum

print ("The maximum temperature registred in celcius is: ", max(rounded_tempCF))

average=sum(rounded_tempCF)/len(rounded_tempCF)

avg = round(average, 2)
print ("The Average of temperatures in celcius is: ", avg)



    





