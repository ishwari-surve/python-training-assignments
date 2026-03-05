import math

#######################################################################
# Function : Euclidean Distance

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

    return Ans


#######################################################################
# Function : KNN Prediction

def MarvellousKNeighboursClassifier():

    border = "-" * 40

    data = [
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':1,'label':'Blue'},
            {'point':'D','X':6,'Y':5,'label':'Blue'}
           ]

    print(border)
    print("KNN Prediction with Different K Values")
    print(border)

#######################################################################
# New Point

    New_point = {'X':2,'Y':2}

#######################################################################
# Distance Calculation

    for d in data:
        d['distance'] = EucDistance(d,New_point)

#######################################################################
# Sorting Data

    sorted_data = sorted(data,key=lambda item:item['distance'])

#######################################################################
# Test Different K

    K_values = [1,3,5]

    print("Prediction Results")
    print(border)

    for k in K_values:

        nearest = sorted_data[:k]

        votes = {}

        for neighbour in nearest:

            label = neighbour['label']
            votes[label] = votes.get(label,0) + 1

        prediction = max(votes,key=votes.get)

        print("K =",k,"→",prediction)

#######################################################################
# Main Function

def main():

    MarvellousKNeighboursClassifier()


if __name__ == "__main__":
    main()