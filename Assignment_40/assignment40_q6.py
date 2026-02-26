import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "--" * 40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset and Analysis")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)
print("Dataset loaded successfully!")

#######################################################################
# Step 2: Feature Selection
#######################################################################

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]        # Independent variables
Y = df["FinalResult"]       # Target variable

#######################################################################
# Step 3: Train-Test Split
#######################################################################

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

print("Data Splitting Done!")

print("X Shape:", X.shape)
print("Y Shape:", Y.shape)

#######################################################################
# Step 4: Model Creation
#######################################################################

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model Successfully Created:", model)

#######################################################################
# Step 5: Model Training
#######################################################################

model.fit(X_train, Y_train)
print("Model Training Completed!")

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)

#######################################################################
# Step 6: Prediction
#######################################################################

y_pred = model.predict(X_test)
print("\nPredicted Values:", y_pred)


#######################################################################
# Step 10: Misclassified Students
#######################################################################

comparison_df = X_test.copy()
comparison_df["Actual"] = Y_test.values
comparison_df["Predicted"] = y_pred

misclassified = comparison_df[
    comparison_df["Actual"] != comparison_df["Predicted"]
]

print("\n" + Border)
print("MISCLASSIFIED STUDENTS")
print(Border)

print(misclassified)

mis_count = len(misclassified)
print("\nNumber of Misclassified Students:", mis_count)

#######################################################################
# Step 11: Pattern Observation
#######################################################################

if mis_count > 0:
    print("\nAverage values of misclassified students:")
    print(misclassified.mean(numeric_only=True))
else:
    print("\nNo misclassified students found.")

print("\nAnalysis Hint:")
print("Misclassification usually occurs near decision boundaries where student performance is borderline.")