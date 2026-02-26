import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

Border = "--" * 40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset")
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
# Step 3: Model Training
#######################################################################

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, Y_train)

print("Model Trained Successfully!")

#######################################################################
# Step 4: Decision Tree Visualization
#######################################################################

print(Border)
print("Step 4: Decision Tree Visualization")
print(Border)

plt.figure(figsize=(15,8))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree for Student Performance")
plt.show()