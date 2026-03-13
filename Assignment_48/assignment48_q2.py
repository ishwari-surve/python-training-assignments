import numpy as np
import math 

Border = "-" * 40

def Mean():
    Data =[6,7,8,9,10,11,12]



    mean =sum(Data)/len(Data)
    print("Mean is :",mean)
    print(Border)

    deviations = []
    for i in Data:
        deviation = i - mean
        deviations.append(deviation)
    print("Deviations are :",deviations)
    print(Border)

    sqrs = []
    for i in deviations:
        square = i * i
        sqrs.append(square)
    print("Xi - X_bar",sqrs)
    print(Border)

    add = 0

    for i in sqrs:
        add = add + i 
    print("Sumation of Xi - X_bar ",add)
    print(Border)

    var = add /len(Data)
    print("Variance is:",var)
    print(Border)

    sd = math.sqrt(var)
    print("Standard Deviation :",sd)
    print(Border)





def main():
    Mean()

if __name__ =="__main__":
    main()
