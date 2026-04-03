import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

#---------------------------------------------------
# Step 1: Load and Explore the Dataset
#---------------------------------------------------
Border = '-'*40

print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("bank-full.csv", sep=";")

print("Shape of Dataset:", df.shape)
print(df.head())
print(df.describe())
print(df.info())

# Handle missing or unknown values
df.replace('unknown', None, inplace=True)
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Display class distribution
print("Class Distribution:")
print(df['y'].value_counts())

# Visualize class distribution
df['y'].value_counts().plot(kind='bar', color=['steelblue', 'salmon'])
plt.title("Class Distribution")
plt.xlabel("Subscribed (yes/no)")
plt.ylabel("Count")
plt.show()

#---------------------------------------------------
# Step 2: Preprocess the Data
#---------------------------------------------------
print(Border)
print("Step 2: Preprocess the Data")
print(Border)

le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

print("After Label Encoding:")
print(df.head())
print(Border)

X = df.drop('y', axis=1)
Y = df['y']

print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)

scaler = StandardScaler()
X = scaler.fit_transform(X)

print("After Scaling:")
print(X[:5])
print(Border)

#---------------------------------------------------
# Step 3: Split the Data
#---------------------------------------------------
print(Border)
print("Step 3:Split the Data")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training set size:", X_train.shape)
print("Testing set size :", X_test.shape)
print(Border)

#---------------------------------------------------
# Step 4: Train Classification Models
#---------------------------------------------------
print(Border)
print("Step 4: Train Classification Models")
print(Border)

model_lr  = LogisticRegression(max_iter=1000)
model_knn = KNeighborsClassifier(n_neighbors=5)
model_rf  = RandomForestClassifier(n_estimators=100, random_state=42)

model_lr.fit(X_train, Y_train)
model_knn.fit(X_train, Y_train)
model_rf.fit(X_train, Y_train)

print("All 3 models trained successfully!")
print(Border)

#---------------------------------------------------
# Step 5: Evaluate the Models
#---------------------------------------------------
print(Border)
print("Step 5: Evaluate the Models")
print(Border)

pred_lr  = model_lr.predict(X_test)
pred_knn = model_knn.predict(X_test)
pred_rf  = model_rf.predict(X_test)

# Accuracy
print("Accuracy:")
print("Logistic Regression :", accuracy_score(Y_test, pred_lr))
print("K-Nearest Neighbors :", accuracy_score(Y_test, pred_knn))
print("Random Forest       :", accuracy_score(Y_test, pred_rf))
print(Border)

# Confusion Matrix
print("Confusion Matrix - Logistic Regression:")
print(confusion_matrix(Y_test, pred_lr))
print(Border)

print("Confusion Matrix - KNN:")
print(confusion_matrix(Y_test, pred_knn))
print(Border)

print("Confusion Matrix - Random Forest:")
print(confusion_matrix(Y_test, pred_rf))
print(Border)

# Classification Report
print("Classification Report - Logistic Regression:")
print(classification_report(Y_test, pred_lr))
print(Border)

print("Classification Report - KNN:")
print(classification_report(Y_test, pred_knn))
print(Border)

print("Classification Report - Random Forest:")
print(classification_report(Y_test, pred_rf))
print(Border)

# ROC-AUC Score
prob_lr  = model_lr.predict_proba(X_test)[:, 1]
prob_knn = model_knn.predict_proba(X_test)[:, 1]
prob_rf  = model_rf.predict_proba(X_test)[:, 1]

print("ROC-AUC Score:")
print("Logistic Regression :", roc_auc_score(Y_test, prob_lr))
print("K-Nearest Neighbors :", roc_auc_score(Y_test, prob_knn))
print("Random Forest       :", roc_auc_score(Y_test, prob_rf))
print(Border)

#---------------------------------------------------
# Step 6: Visualize Results
#---------------------------------------------------

print(Border)
print("Step 6: Visualize Results")


# Plot Confusion Matrix
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.heatmap(confusion_matrix(Y_test, pred_lr),  annot=True, fmt='d', ax=axes[0])
axes[0].set_title("Confusion Matrix - Logistic Regression")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

sns.heatmap(confusion_matrix(Y_test, pred_knn), annot=True, fmt='d', ax=axes[1])
axes[1].set_title("Confusion Matrix - KNN")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

sns.heatmap(confusion_matrix(Y_test, pred_rf),  annot=True, fmt='d', ax=axes[2])
axes[2].set_title("Confusion Matrix - Random Forest")
axes[2].set_xlabel("Predicted")
axes[2].set_ylabel("Actual")

plt.show()

# Plot ROC Curves
fpr_lr,  tpr_lr,  _ = roc_curve(Y_test, prob_lr)
fpr_knn, tpr_knn, _ = roc_curve(Y_test, prob_knn)
fpr_rf,  tpr_rf,  _ = roc_curve(Y_test, prob_rf)

plt.plot(fpr_lr,  tpr_lr,  label="Logistic Regression")
plt.plot(fpr_knn, tpr_knn, label="KNN")
plt.plot(fpr_rf,  tpr_rf,  label="Random Forest")
plt.plot([0, 1], [0, 1], 'k--', label="No skill")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves")
plt.legend()
plt.grid(True)
plt.show()
print(Border)

