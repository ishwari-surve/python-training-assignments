import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "--"*40

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

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, Y_train)

print("Model trained successfully")


print(Border)
print("Create New DataFrame")
print(Border)

new_students = pd.DataFrame({
    "StudyHours": [5,6,7,2,3],
    "Attendance": [88,92,98,65,53],
    "PreviousScore": [59,48,22,67,89],
    "AssignmentsCompleted": [5,6,3,4,5],
    "SleepHours": [7,6,8,5,6]
})

print(new_students)


print(Border)
print("Prediction")
print(Border)

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions

print(new_students)

print("1 = Pass")
print("0 = Fail")
