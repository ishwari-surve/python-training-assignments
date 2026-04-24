import math

print("\n===================================================")
print("     PROGRAM 1 : SINGLE ARTIFICIAL NEURON")
print("===================================================\n")

# Step 1: Input Values
x1   = 2
x2   = 3
w1   = 0.4
w2   = 0.6
bias = 0.5

print("STEP 1 : INPUT VALUES")
print("----------------------")
print(f"  x1   = {x1}")
print(f"  x2   = {x2}")
print(f"  w1   = {w1}")
print(f"  w2   = {w2}")
print(f"  bias = {bias}")

# Step 2: Calculate Weighted Sum
print("\nSTEP 2 : CALCULATE WEIGHTED SUM")
print("---------------------------------")
print("Formula : z = (x1*w1) + (x2*w2) + bias")

m1 = x1 * w1
m2 = x2 * w2

print(f"\n  x1 * w1 = {x1} * {w1} = {m1}")
print(f"  x2 * w2 = {x2} * {w2} = {m2}")

z = m1 + m2 + bias
print(f"\n  z = {m1} + {m2} + {bias} = {z}")

# Step 3: Apply Sigmoid Activation
print("\nSTEP 3 : APPLY SIGMOID ACTIVATION")
print("-----------------------------------")
print("Formula : sigmoid(z) = 1 / (1 + e^(-z))")

output = 1 / (1 + math.exp(-z))
print(f"\n  sigmoid({z}) = {output:.4f}")

# Step 4: Final Output
print("\nSTEP 4 : FINAL OUTPUT")
print("----------------------")
print(f"  Weighted Sum (z) : {z}")
print(f"  Final Output (y) : {output:.4f}")
print(f"  Confidence (%)   : {output * 100:.2f}%")

print("\nDecision Rule:")
print("  If output >= 0.5 → Close to 1 → Positive Class")
print("  If output <  0.5 → Close to 0 → Negative Class")

if output >= 0.5:
    print(f"\nResult : Output {output:.4f} is close to 1 → Positive Class")
else:
    print(f"\nResult : Output {output:.4f} is close to 0 → Negative Class")