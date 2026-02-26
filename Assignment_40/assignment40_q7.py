import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "--" * 40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

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

X = df[feature_cols]
Y = df["FinalResult"]

#######################################################################
# Step 3: Compare Different random_state Values
#######################################################################

print("\n" + Border)
print("Step 3: Comparing Different random_state Values")
print(Border)

random_states = [0, 10, 42]

for state in random_states:

    print("\nUsing random_state =", state)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=state
    )

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=state
    )

    model.fit(X_train, Y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, y_pred)

    print("Testing Accuracy:", accuracy * 100)