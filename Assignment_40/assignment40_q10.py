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
# Step 2: Train-Test Split
#######################################################################

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

#######################################################################
# Step 3: Train Model with max_depth=None
#######################################################################

print(Border)
print("Step 3: Training Model with max_depth=None")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    random_state=42
)

model.fit(X_train, Y_train)

#######################################################################
# Step 4: Training Accuracy
#######################################################################

train_pred = model.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_pred)

print("Training Accuracy:", train_accuracy * 100)

#######################################################################
# Step 5: Testing Accuracy
#######################################################################

test_pred = model.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_pred)

print("Testing Accuracy:", test_accuracy * 100)