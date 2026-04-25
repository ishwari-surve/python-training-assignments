import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("\n===================================================")
print("     PROGRAM 2 : LOAN APPROVAL PREDICTION")
print("===================================================\n")

# Task 1: Preprocess Categorical Values
print("TASK 1 : PREPROCESS CATEGORICAL VALUES")
print("----------------------------------------")

X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000,  8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000,  9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

X = np.array(X)
y = np.array(y)

print(f"  Total Samples : {len(X)}")
print(f"  Features      : Income, Credit Score, Loan Amount, EMI, Employment Status")
print(f"  Output        : 0 = Rejected, 1 = Approved")
print(f"\n  Employment Status (Categorical):")
print(f"  0 = Not Stable")
print(f"  1 = Stable")
print(f"\n  Already converted to 0 and 1 (no further encoding needed)")

# Task 2: Apply Scaling
print("\nTASK 2 : APPLY SCALING")
print("-----------------------")

scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("  StandardScaler applied successfully")
print(f"  Before Scaling X[0] : {X[0]}")
print(f"  After  Scaling X[0] : {X_scaled[0].round(4)}")

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print(f"\n  Training Samples : {len(X_train)}")
print(f"  Testing Samples  : {len(X_test)}")

# Task 3: Train FNN Model
print("\nTASK 3 : TRAIN FNN MODEL")
print("-------------------------")

model = Sequential()
model.add(Dense(16, activation='relu', input_dim=5))
model.add(Dense(8,  activation='relu'))
model.add(Dense(1,  activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print("  Model Architecture:")
print("  Input  Layer : 5 neurons (one per feature)")
print("  Hidden Layer : 16 neurons (ReLU)")
print("  Hidden Layer : 8  neurons (ReLU)")
print("  Output Layer : 1  neuron  (Sigmoid)")

model.fit(X_train, y_train, epochs=100, verbose=0)
print("\n  Model trained successfully for 100 epochs!")

# Task 4: Evaluate Model
print("\nTASK 4 : EVALUATE MODEL")
print("------------------------")

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"  Test Loss     : {loss:.4f}")
print(f"  Test Accuracy : {accuracy * 100:.2f}%")

# Task 5: Predict New Applicant
print("\nTASK 5 : PREDICT NEW APPLICANT")
print("--------------------------------")

new_applicant = [[55000, 720, 400000, 10000, 1]]
new_applicant_scaled = scaler.transform(new_applicant)
prediction = model.predict(new_applicant_scaled, verbose=0)

print(f"  New Applicant Data:")
print(f"  Income={55000}, Credit Score={720}, Loan={400000}, EMI={10000}, Employment=Stable")
print(f"\n  Prediction Score : {prediction[0][0]:.4f}")

if prediction[0][0] >= 0.5:
    print("  Prediction       : Loan APPROVED ")
else:
    print("  Prediction       : Loan REJECTED ")
