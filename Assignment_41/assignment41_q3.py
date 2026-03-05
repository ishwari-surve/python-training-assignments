import math

#######################################################################
# Function : Euclidean Distance


def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

    return Ans


#######################################################################
# Function : MarvellousKNeighboursClassifier


def MarvellousKNeighboursClassifier():

    border = "-" * 40

    data = [
            {'X':2,'Y':60,'label':'Fail'},
            {'X':5,'Y':80,'label':'Pass'},
            {'X':6,'Y':85,'label':'Pass'},
            {'X':1,'Y':50,'label':'Fail'}
           ]

    print(border)
    print("KNN Student Pass/Fail Prediction")
    print(border)

    print("Training Dataset")
    print(border)

    for i in data:
        print(i)

    print(border)

#######################################################################
# Accept Input From User

    StudyHours = int(input("Enter Study Hours : "))
    Attendance = int(input("Enter Attendance :  "))

    New_point = {'X':StudyHours,'Y':Attendance}

#######################################################################
# Distance Calculation

    for d in data:
        d['distance'] = EucDistance(d,New_point)

    print(border)
    print("Calculated Distances")
    print(border)

    for d in data:
        print(d)

#######################################################################
# Sorting Data

    sorted_data = sorted(data,key=lambda item:item['distance'])

#######################################################################
# Select K Neighbours

    k = 3
    nearest = sorted_data[:k]

#######################################################################
# Voting

    votes = {}

    for neighbour in nearest:

        label = neighbour['label']

        votes[label] = votes.get(label,0) + 1

#######################################################################
# Prediction

    prediction = max(votes,key=votes.get)

    print(border)
    print("Predicted Result :",prediction)
    print(border)


#######################################################################
# Main Function
#######################################################################

def main():

    MarvellousKNeighboursClassifier()


if __name__ == "__main__":
    main()