import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#-----------------------------------------
# Part 1: Data Preprocessing
#-----------------------------------------

Border = "-"*50
# 1. Load both datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

print("Datasets loaded successfully")
print("Fake shape :", fake.shape)
print("True shape :", true.shape)

# 2. Add label column
fake["label"] = 0   # Fake news
true["label"] = 1   # Real news

# 3. Combine both datasets
df = pd.concat([fake, true], axis=0)

print("\nCombined dataset shape:", df.shape)

# 4. Check null values
print("\nNull Values:")
print(df.isnull().sum())

# 5. Drop null values
df = df.dropna()

print("\nAfter removing null values:", df.shape)

# 6. Select useful column (text)
df = df[["text", "label"]]

print("\nFinal dataset preview:")
print(df.head())

print(Border)

#-----------------------------------------
# Part 2: Feature Extraction (TF-IDF)
#-----------------------------------------

Border = "-"*50
# Separate Features and Target
X = df["text"]
Y = df["label"]

print("Features and Target separated")
print("X shape:", X.shape)
print("Y shape:", Y.shape)

# Apply TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

X = vectorizer.fit_transform(X)

print("\nText converted into TF-IDF features")
print("New shape of X:", X.shape)
print(Border)

#-----------------------------------------
# Part 3: Model Training + Voting Classifier
#-----------------------------------------

Border = "-"*50
# 1. Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training size:", X_train.shape)
print("Testing size :", X_test.shape)

# 2. Create Models
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier()

# 3. Train Individual Models
lr.fit(X_train, Y_train)
dt.fit(X_train, Y_train)

print("\nIndividual models trained successfully")

# 4. Hard Voting Classifier
voting_hard = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='hard'
)

voting_hard.fit(X_train, Y_train)

# 5. Soft Voting Classifier
voting_soft = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='soft'
)

voting_soft.fit(X_train, Y_train)

print("Voting models trained successfully")

print(Border)

#-----------------------------------------
# Part 4: Evaluation
#-----------------------------------------

Border = "-"*50
# Predictions
pred_lr   = lr.predict(X_test)
pred_dt   = dt.predict(X_test)
pred_hard = voting_hard.predict(X_test)
pred_soft = voting_soft.predict(X_test)

#-----------------------------------------
# 1. Compare Accuracy
#-----------------------------------------

print("Accuracy Comparison:")
print("Logistic Regression :", accuracy_score(Y_test, pred_lr))
print("Decision Tree       :", accuracy_score(Y_test, pred_dt))
print("Hard Voting         :", accuracy_score(Y_test, pred_hard))
print("Soft Voting         :", accuracy_score(Y_test, pred_soft))

print(Border)

#-----------------------------------------
# 2. Confusion Matrices
#-----------------------------------------

cm_lr   = confusion_matrix(Y_test, pred_lr)
cm_dt   = confusion_matrix(Y_test, pred_dt)
cm_hard = confusion_matrix(Y_test, pred_hard)
cm_soft = confusion_matrix(Y_test, pred_soft)

print("Confusion Matrix - Logistic Regression:\n", cm_lr)
print("Confusion Matrix - Decision Tree:\n", cm_dt)
print("Confusion Matrix - Hard Voting:\n", cm_hard)
print("Confusion Matrix - Soft Voting:\n", cm_soft)

print(Border)

#-----------------------------------------
# 3. Classification Report
#-----------------------------------------

print("Classification Report - Logistic Regression:")
print(classification_report(Y_test, pred_lr))

print("Classification Report - Decision Tree:")
print(classification_report(Y_test, pred_dt))

print("Classification Report - Hard Voting:")
print(classification_report(Y_test, pred_hard))

print("Classification Report - Soft Voting:")
print(classification_report(Y_test, pred_soft))

print(Border)

#-----------------------------------------
# 4. Visualization 
#-----------------------------------------

fig, axes = plt.subplots(1, 4, figsize=(18,4))

sns.heatmap(cm_lr, annot=True, fmt='g', ax=axes[0])
axes[0].set_title("Logistic Regression")

sns.heatmap(cm_dt, annot=True, fmt='g', ax=axes[1])
axes[1].set_title("Decision Tree")

sns.heatmap(cm_hard, annot=True, fmt='g', ax=axes[2])
axes[2].set_title("Hard Voting")

sns.heatmap(cm_soft, annot=True, fmt='g', ax=axes[3])
axes[3].set_title("Soft Voting")

plt.show()

print(Border)