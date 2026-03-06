import matplotlib.pyplot as plt

def LinearRegressionExample():

    Border = "-"*60

    # Dataset
    X = [1,2,3,4,5]           # Experience
    Y = [20000,25000,30000,35000,40000]   # Salary

    print(Border)
    print("Experience:",X)
    print("Salary:",Y)
    print(Border)

    # Mean
    meanX = sum(X)/len(X)
    meanY = sum(Y)/len(Y)

    print("Mean X:",meanX)
    print("Mean Y:",meanY)

    print(Border)

    # Calculate (X-Xbar)(Y-Ybar)
    numerator = 0
    denominator = 0

    for x,y in zip(X,Y):

        numerator += (x-meanX)*(y-meanY)
        denominator += (x-meanX)**2

    # Slope
    m = numerator/denominator

    # Intercept
    c = meanY - m*meanX

    print("Slope (m):",m)
    print("Intercept (c):",c)

    print(Border)

    # Prediction for 6 years
    x_new = 6
    y_pred = m*x_new + c

    print("Predicted Salary for 6 years experience:",y_pred)

    print(Border)

    # Plot regression line
    predicted_line = []

    for i in X:
        predicted_line.append(m*i + c)

    plt.scatter(X,Y)
    plt.plot(X,predicted_line)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Linear Regression Salary Prediction")

    plt.show()


def main():
    LinearRegressionExample()

if __name__ == "__main__":
    main()