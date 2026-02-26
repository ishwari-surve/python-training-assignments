#Q5
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "--"*40

#######################################################################
print(Border)
print("Step 1: Load Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]


#######################################################################
print(Border)
print("Step 2: Train Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)


#######################################################################
print(Border)
print("Step 3: Model Training")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, Y_train)

y_pred = model.predict(X_test)


#######################################################################
print(Border)
print("Step 4: Accuracy Using Sklearn")
print(Border)

sklearn_accuracy = accuracy_score(Y_test, y_pred)

print("Sklearn Accuracy :", sklearn_accuracy * 100)


#######################################################################
print(Border)
print("Step 5: Manual Accuracy Calculation")
print(Border)

correct_predictions = 0

for actual, predicted in zip(Y_test, y_pred):
    if actual == predicted:
        correct_predictions += 1

manual_accuracy = correct_predictions / len(Y_test)

print("Manual Accuracy :", manual_accuracy * 100)


#######################################################################
print(Border)
print("Verification")
print(Border)

if round(sklearn_accuracy,4) == round(manual_accuracy,4):
    print("Manual Accuracy matches Sklearn Accuracy")
else:
    print("Mismatch in Accuracy Calculation")
