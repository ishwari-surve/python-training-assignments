# Assignment 49 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,f1_score

#--------------------------------------------------------
#Step :1 EDA
#--------------------------------------------------------

Border = '-'*40

print(Border)
print("Step 1: EDA")
print(Border)

df = pd.read_csv("diabetes.csv")

print("First 5 rows")
print(df.head())
print(Border)

print("\n Null values")
print(df.isnull().sum())
print(Border)

print("\n Column info")
print(df.info())
print(Border)

print("\n Basic Statistics")
print(df.describe())
print(Border)

plt.hist(df['Outcome'])
plt.title("Distribution of Target varible(Outcome)")
plt.xlabel("0 for no diabetes")
plt.ylabel("1 for Diabetes")
plt.show()
print(Border)

#--------------------------------------------------------
#Step 2 : Data Preprocessing
#--------------------------------------------------------
print(Border)
print("Step 2: Data Preprocessing")
print(Border)

cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

for col in cols:
    print(col,":",(df[col] == 0).sum())

df[cols]=df[cols].replace(0,np.nan)
df.fillna(df.mean(),inplace=True)

df.dropna(inplace=True)
print(df.isnull().sum())

X = df.drop("Outcome",axis = 1)
Y = df['Outcome']

scaler = StandardScaler()
X_scale = scaler.fit_transform(X)

print("Features (X):")
print(X.head())
print(Border)

print("\nTarget (Y):")
print(Y.head())
print(Border)

print("Standard Scaler Data X :")
print(X_scale)

print(Border)

#--------------------------------------------------------
#Step 3: Train Models
#--------------------------------------------------------

print(Border)
print("Step 3: Train Models")
print(Border)

X_train,X_test, Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model_lr = LogisticRegression()
model_lr.fit(X_train,Y_train)
Y_pred = model_lr.predict(X_test)

print("Accuracy of Logistic Regression: ")
print(accuracy_score(Y_pred,Y_test)*100)

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train,Y_train)
Y_pred_knn = model_knn.predict(X_test)

print("Accuracy of KNN: ")
print(accuracy_score(Y_pred_knn,Y_test)*100)

print(Border)

#--------------------------------------------------------
#Step 4: Model Evaluation (precision, recall, and F1 score.)
#--------------------------------------------------------

print("Step 4 : Model Evaluation (precision, recall, and F1 score.)")
print(Border)

print("Accuracy of Logistic Regression: ")
print(accuracy_score(Y_pred,Y_test)*100)

print("\n Classification Report of Logistic Regression:")
print(classification_report(Y_test,Y_pred))
print(Border)

print("Accuracy of KNN: ")
print(accuracy_score(Y_pred_knn,Y_test)*100)

print("\n Classification Report of KNN:")
print(classification_report(Y_test,Y_pred_knn))
print(Border)

cm_lr = confusion_matrix(Y_test,Y_pred)
cm_knn = confusion_matrix(Y_test,Y_pred)

print("\n Confusion Matrix Logistic Regression")
print(cm_lr)
print(Border)

print("\n Confusion Matrix KNN")
print(cm_knn)
print(Border)

sns.heatmap(cm_lr, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

sns.heatmap(cm_knn, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

#--------------------------------------------------------
#Step 5 : Final Output
#--------------------------------------------------------
print("Step 5: Final Output")
print(Border)

print("Predictions:")
print(Y_pred)
print(Border)

results = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": Y_pred
})

print("\nResults:")
print(results.head())
print(Border)

results.to_csv("diabetes_predictions.csv", index=False)

print("\nPredictions saved to diabetes_predictions.csv")
print(Border)






