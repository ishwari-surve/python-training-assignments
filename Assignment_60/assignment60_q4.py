import math

print("\n===================================================")
print("  PROGRAM 4 : WEIGHT UPDATE IN ANN")
print("===================================================\n")

# Step 1: Input Values
x             = 2.0
weight        = 0.5
bias          = 0.1
target        = 1.0
learning_rate = 0.1

print("STEP 1 : INPUT VALUES")
print("----------------------")
print(f"  Input (x)          : {x}")
print(f"  Weight (w)         : {weight}")
print(f"  Bias (b)           : {bias}")
print(f"  Target Output (y)  : {target}")
print(f"  Learning Rate      : {learning_rate}")

# Step 2: Calculate Prediction
print("\nSTEP 2 : CALCULATE PREDICTION")
print("--------------------------------")
print("Formula : z = x * weight + bias")
print("          prediction = sigmoid(z)")

z          = x * weight + bias
prediction = 1 / (1 + math.exp(-z))

print(f"\n  z          = {x} * {weight} + {bias} = {z}")
print(f"  prediction = sigmoid({z}) = {prediction:.4f}")

# Step 3: Calculate Error
print("\nSTEP 3 : CALCULATE ERROR")
print("--------------------------")
print("Formula : error = target - prediction")

error = target - prediction
print(f"\n  error = {target} - {prediction:.4f} = {error:.4f}")

# Step 4: Update Weight using Gradient Descent
print("\nSTEP 4 : UPDATE WEIGHT (GRADIENT DESCENT)")
print("--------------------------------------------")
print("Formula : new_weight = old_weight + (learning_rate * error * x)")
print("          new_bias   = old_bias   + (learning_rate * error)")

new_weight = weight + (learning_rate * error * x)
new_bias   = bias   + (learning_rate * error)

print(f"\n  new_weight = {weight} + ({learning_rate} * {error:.4f} * {x}) = {new_weight:.4f}")
print(f"  new_bias   = {bias}   + ({learning_rate} * {error:.4f})        = {new_bias:.4f}")

# Step 5: Display Old vs New
print("\nSTEP 5 : OLD vs UPDATED WEIGHT")
print("--------------------------------")
print(f"  Old Weight : {weight}")
print(f"  New Weight : {new_weight:.4f}")
print(f"  Old Bias   : {bias}")
print(f"  New Bias   : {new_bias:.4f}")

print("\nConclusion:")
print("  Weight updated to reduce error")
print("  This process repeats during training")
print("  Each update makes prediction closer to target")
print("  This is called GRADIENT DESCENT ✅")