import math

print("\n===================================================")
print("     PROGRAM 3 : CALCULATE LOSS MANUALLY")
print("===================================================\n")

# Step 1: Actual and Predicted Values
actual    = [1, 0, 1, 0, 1]
predicted = [0.9, 0.1, 0.8, 0.2, 0.7]

print("STEP 1 : ACTUAL AND PREDICTED VALUES")
print("--------------------------------------")
print(f"  Actual    : {actual}")
print(f"  Predicted : {predicted}")

# Step 2: Mean Squared Error
print("\nSTEP 2 : MEAN SQUARED ERROR (MSE)")
print("------------------------------------")
print("Formula : MSE = (1/n) * sum((actual - predicted)^2)")

mse_sum = 0
for i in range(len(actual)):
    error   = actual[i] - predicted[i]
    squared = error ** 2
    mse_sum += squared
    print(f"  ({actual[i]} - {predicted[i]})^2 = {squared:.4f}")

mse = mse_sum / len(actual)
print(f"\n  MSE = {mse_sum:.4f} / {len(actual)} = {mse:.4f}")

# Step 3: Binary Cross Entropy
print("\nSTEP 3 : BINARY CROSS ENTROPY (BCE)")
print("--------------------------------------")
print("Formula : BCE = -(1/n) * sum(y*log(p) + (1-y)*log(1-p))")

bce_sum = 0
for i in range(len(actual)):
    y    = actual[i]
    p    = predicted[i]
    loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
    bce_sum += loss
    print(f"  y={y}, p={p} → loss = {loss:.4f}")

bce = bce_sum / len(actual)
print(f"\n  BCE = {bce_sum:.4f} / {len(actual)} = {bce:.4f}")

# Step 4: Display Results
print("\nSTEP 4 : FINAL RESULTS")
print("-----------------------")
print(f"  Mean Squared Error (MSE)   : {mse:.4f}")
print(f"  Binary Cross Entropy (BCE) : {bce:.4f}")

# Step 5: Explanation
print("\nSTEP 5 : WHICH LOSS FUNCTION TO USE")
print("--------------------------------------")
print("MSE (Mean Squared Error):")
print("  Used for : REGRESSION problems")
print("  Example  : Predicting house price, marks, temperature")

print("\nBCE (Binary Cross Entropy):")
print("  Used for : CLASSIFICATION problems")
print("  Example  : Predicting diabetic or not, spam or not")