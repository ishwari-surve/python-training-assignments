#Q1 DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier


Border = "-" * 40

########################################################
# Step 1: Load the dataset
########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")

########################################################
# Step 2 : Decide Independent and Dependent variables
########################################################

print(Border)
print("Step 2 : Decide Independent and Dependent variables")
print(Border)


feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]    #Independent 
Y = df["FinalResult"]   #Dependent

print("X shape :", X.shape)
print("Y shape :", Y.shape)


########################################################
# Step 3 : Split the dataset for training and testing
########################################################

print(Border)
print("Step 3 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,  #0.2 means 20%
    random_state=42
)

print("Data splitting completed....")

print("X - Independent :",X.shape)
print("Y - Independent :",Y.shape)

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)

print("Y_train :", Y_train.shape)
print("Y_test  :", Y_test.shape)


########################################################
# Step 4 : Build the model
########################################################

print(Border)
print("Step 4 : Build the model")
print(Border)

print("We are using DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model created successfully :", model)


########################################################
# Step 5 : Train the model
########################################################

print(Border)
print("Step 5 : Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed successfully!!")
