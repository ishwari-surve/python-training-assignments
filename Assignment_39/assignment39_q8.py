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
# Step 3: Data Visualization
#######################################################################

print(Border)
print("Step 3: Data Visualization")
print(Border)

#Scatter Plot shows relationship between StudyHours and PreviousScore
plt.figure(figsize=(7,5))
sns.scatterplot(
    x="StudyHours",
    y="PreviousScore",
    hue="FinalResult",
    data=df
)

plt.title("StudyHours vs PreviousScore")
plt.grid(True)
plt.show()

#Boxplot shows StudyHours distribution for Pass/Fail
plt.figure(figsize=(7,5))

sns.boxplot(
    x="FinalResult",
    y="StudyHours",
    data=df
)

plt.title("FinalResult vs StudyHours")
plt.grid(True)
plt.show()

#Histogram shows overall distribution of StudyHours
plt.figure(figsize=(7,5))
plt.hist(
    df["StudyHours"],
    bins=10
)

plt.title("Distribution of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

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

#######################################################################
# Step 6: Prediction
#######################################################################

print(Border)
print("Step 3: Predicting and Displaying result for X_test")
print(Border)

y_pred = model.predict(X_test)
print("Predicted Values",y_pred)

#######################################################################
# Step 7: Accuracy Calculation
#######################################################################

print(Border)
print("Step 7: Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test,y_pred)
print("Your Accuracy is: ",accuracy*100)

#######################################################################
# Step 8: Confusion Matrix Generation
#######################################################################

print(Border)
print("Step8: Confusion Matrix Generation")
print(Border)

cm = confusion_matrix(Y_test,y_pred)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix for Student Dataset")
plt.show()

#######################################################################
# Step 9: Final Conclusion
#######################################################################
print(Border)
print("Final Conclusion")
print(Border)

if accuracy > 0.85:
    print("Model performs very well")
elif accuracy > 0.70:
    print("Model performs reasonably well")
else:
    print("Model needs improvement")

print("Decision Tree successfully predicts student performance")