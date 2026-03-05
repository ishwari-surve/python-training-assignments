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
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':1,'label':'Blue'},
            {'point':'D','X':6,'Y':5,'label':'Blue'}
           ]

    print(border)
    print("Marvellous Userdefined KNN")
    print(border)


    for i in data:
        print(i)

    print(border)

#######################################################################
# New Point : 


    New_point = {'X':2,'Y':2}

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

    print(border)
    print("Sorted Data")
    print(border)

    for d in sorted_data:
        print(d)

#######################################################################
# Select K Neighbours

    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 Neighbours")
    print(border)

    for d in nearest:
        print(d)

#######################################################################
# Voting


    votes = {}

    for neighbour in nearest:

        label = neighbour['label']

        votes[label] = votes.get(label,0) + 1

    print(border)
    print("Voting Result")
    print(border)

    for d in votes:
        print("Class :",d,"Votes :",votes[d])

#######################################################################
# Prediction


    prediction = max(votes,key=votes.get)

    print(border)
    print("Predicted Class :",prediction)
    print(border)


#######################################################################
# Main Function


def main():

    MarvellousKNeighboursClassifier()


if __name__ == "__main__":
    main()