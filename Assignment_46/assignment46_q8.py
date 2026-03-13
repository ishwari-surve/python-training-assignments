import numpy as np
from sklearn.linear_model import LinearRegression

def LR():
    StudyHours = np.array([1,2,3,4,5]).reshape(-1,1)
    Marks = np.array([50,55,60,65,70])

    print("Independent variables",StudyHours)
    print("Dependent variables",Marks)

    model = LinearRegression()
    model.fit(StudyHours,Marks)

    print("Coefficient :",model.coef_)

    print("intercept",model.intercept_)

    StudyHours_new = np.array([[6]])

    pred = model.predict(StudyHours_new)

    print("Predicted marks",pred)


def main():
    LR()



if __name__ == "__main__":
    main()

