import numpy as np
from sklearn.linear_model import LinearRegression

def LR():
    StudyHours = [1,2,3,4,5]
    SleepHours = [7,6,7,6,8]
    Marks = [50,55,60,65,70]

    x = np.array(list(zip(StudyHours,SleepHours)))

    y = np.array(Marks)

    
    

    print("Independent variables",x)
    print("Dependent variables",y)

    model = LinearRegression()
    model.fit(x,y)

    print("Coefficient of StudyHours:",model.coef_[0])
    print("Coefficient of SleepHpurs:",model.coef_[1])

    print("intercept",model.intercept_)

    


def main():
    LR()



if __name__ == "__main__":
    main()
