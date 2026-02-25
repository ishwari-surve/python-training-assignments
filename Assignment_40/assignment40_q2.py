import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "--"*40

#######################################################################
# Step 1: Load the Dataset and Analysis
#######################################################################

print(Border)
print("Step 1: Load the Dataset and Analysis")
print(Border)

DatasetPath = "student_performance_ml.csv"  

df = pd.read_csv(DatasetPath)
print("Datasets get loaded Successfully!!!!!")

feature_cols=[              
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X = df[feature_cols]        #Independent variables
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,       # 0.3 means 30%
    random_state=42      # Shuffle the Data
)

print("Data Splitting Activity Done!!!!!")

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape) 

model = DecisionTreeClassifier(         
    criterion="gini",
    max_depth=3,            #hyper parameter tuning
    random_state=42 
)

print("Model Successfully Created: ",model)

model.fit(X_train,Y_train)

print("Model Training Completed!!!!!")


print("X_train :",X_train.shape)
print("X_test :",X_test.shape)   

print("Y_train :",Y_train.shape)    
print("Y_test :",Y_test.shape)     

y_pred = model.predict(X_test)
print("Predicted Values",y_pred)

accuracy = accuracy_score(Y_test,y_pred)    #Finding Accuracy
print("Your Accuracy is: ",accuracy*100)

#Yes affects the accuracy
#Previous accuracy was 91.66666 and after removing SleepHours from the dataset it is showig  88.88888888888889