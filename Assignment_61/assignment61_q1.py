import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("\n===================================================")
print("  PROGRAM 1 : CUSTOMER CHURN PREDICTION")
print("===================================================\n")

# Task 1: Load / Create Dataset
print("TASK 1 : LOAD DATASET")
print("----------------------")

X = [
    [25, 500,  12, 1, 2],
    [30, 700,  24, 0, 1],
    [45, 1200,  6, 5, 8],
    [50, 1500,  5, 6, 10],
    [28, 600,  18, 1, 1],
    [35, 800,  30, 0, 0],
    [48, 1400,  4, 7, 9],
    [52, 1600,  3, 8, 12],
    [27, 550,  20, 0, 1],
    [42, 1300,  8, 4, 7]
]

y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

X = np.array(X)
y = np.array(y)

print(f"  Total Samples : {len(X)}")
print(f"  Features      : Age, Monthly Charges, Tenure, Complaints, Support Calls")
print(f"  Output        : 0 = Stay, 1 = Leave")

# Task 2: Clean Dataset
print("\nTASK 2 : CLEAN DATASET")
print("-----------------------")
print("  No null values in manual dataset")
print("  Data is ready for processing")

# Task 3: Apply StandardScaler
print("\nTASK 3 : APPLY STANDARD SCALER")
print("--------------------------------")

scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("  Scaling applied successfully")
print(f"  Before Scaling X[0] : {X[0]}")
print(f"  After  Scaling X[0] : {X_scaled[0].round(4)}")

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
print(f"\n  Training Samples : {len(X_train)}")
print(f"  Testing Samples  : {len(X_test)}")

# Task 4: Train FNN Model
print("\nTASK 4 : TRAIN FNN MODEL")
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

# Task 5: Evaluate Accuracy
print("\nTASK 5 : EVALUATE ACCURACY")
print("----------------------------")

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"  Test Loss     : {loss:.4f}")
print(f"  Test Accuracy : {accuracy * 100:.2f}%")

# Predict New Customer
print("\nTEST INPUT : NEW CUSTOMER PREDICTION")
print("--------------------------------------")

new_customer = [[46, 1450, 5, 6, 9]]
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled, verbose=0)

print(f"  New Customer Data : Age=46, Charges=1450, Tenure=5, Complaints=6, Calls=9")
print(f"  Prediction Score  : {prediction[0][0]:.4f}")

if prediction[0][0] >= 0.5:
    print("  Prediction        : Customer may LEAVE ")
else:
    print("  Prediction        : Customer will STAY ")