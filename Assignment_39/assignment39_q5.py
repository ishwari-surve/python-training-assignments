import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

Border = "-" * 40

########################################################
# Step 1 : Load the dataset
########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully...")


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

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)


########################################################
# Step 3 : Split the dataset
########################################################

print(Border)
print("Step 3 : Split the dataset")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.4,
    random_state=42
)

print("Data splitting completed")


########################################################
# Step 4 : Build and Train the model
########################################################

print(Border)
print("Step 4 : Build and Train the model")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, Y_train)

print("Model training completed")


########################################################
# Step 5 : Calculate Training and Testing Accuracy
########################################################

print(Border)
print("Step 5 : Training and Testing Accuracy")
print(Border)


train_pred = model.predict(X_train)    # Train accuracy
train_accuracy = accuracy_score(Y_train, train_pred)
print("Training Accuracy : ",(train_accuracy*100 ))


test_pred = model.predict(X_test)                  # Testing accuracy
test_accuracy = accuracy_score(Y_test, test_pred)
print("Testing Accuracy  : ",(test_accuracy*100 ))

# Step 5.1 : Check Overfitting or Underfitting


