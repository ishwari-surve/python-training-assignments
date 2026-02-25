import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "--"*40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

DatasetPath = "student_performance_ml.csv" #Giving the path of dataset

df = pd.read_csv(DatasetPath)
print("Datasets get loaded Successfully!!!!!")

#######################################################################
# Step 2: Data Analysis
#######################################################################

print(Border)
print("Step2: Data Analysis")
print(Border)

#Select feature columns (Independent variables)
feature_cols=[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

#Separate X and Y
X = df[feature_cols]        #Independent variables
Y = df["FinalResult"]       #dependent variables

#Check dataset shape
print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)



#######################################################################
# Step 4: Train and Test Split
#######################################################################

print(Border)
print("Step 4: Train and Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.4,       # 0.4 means 40%
    random_state=42      # Shuffle the Data
)

print("Data Splitting Activity Done!!!!!")

print("X - Independent :",X.shape)  
print("Y - Dependent :",Y.shape)   

print("X_train :",X_train.shape)   
print("X_test :",X_test.shape)      

print("Y_train :",Y_train.shape)    
print("Y_test :",Y_test.shape)      

#######################################################################
# Step 5: Model Training
#######################################################################

print(Border)
print("Step 5: Model Training")
print(Border)

print(" I am using DecisionTreeClassifier") 

#Actual Model Implementation

model = DecisionTreeClassifier(         
    criterion="gini",
    max_depth=3,            #hyper parameter tuning
    random_state=42
)

print("Model Successfully Created: ",model)

model.fit(X_train,Y_train)

print("Model Training Completed!!!!!")

importances = model.feature_importances_


feature_names = X_train.columns
feature_importance_df = pd.DataFrame({"Feature": feature_names,"Importance":importances })
feature_importance_df = feature_importance_df.sort_values(by="Importance",ascending=False)
print(feature_importance_df)



# Attendance feature contributed the most in Predicting final result
# StudyHours,PreviousScore,AssignmentsCompleted and SleepHours contributes least feature