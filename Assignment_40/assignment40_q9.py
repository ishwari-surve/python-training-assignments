import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "--" * 40

#######################################################################
# Step 1: Load Dataset
#######################################################################

print(Border)
print("Step 1: Load Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset Loaded Successfully!")

#######################################################################
# Step 2: Create New Column (PerformanceIndex)
#######################################################################

print(Border)
print("Step 2: Creating PerformanceIndex Column")
print(Border)

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

print(df[["StudyHours", "Attendance", "PerformanceIndex"]].head())

#######################################################################
# Step 3: Feature Selection (Including New Feature)
#######################################################################

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]

X = df[feature_cols]
Y = df["FinalResult"]

#######################################################################
# Step 4: Train-Test Split
#######################################################################

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

#######################################################################
# Step 5: Model Training
#######################################################################

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, Y_train)

print("Model Trained Successfully!")

#######################################################################
# Step 6: Accuracy Checking
#######################################################################

y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)

print(Border)
print("Accuracy After Adding PerformanceIndex:")
print(Border)

print("Accuracy:", accuracy * 100)