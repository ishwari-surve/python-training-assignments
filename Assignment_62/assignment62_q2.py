import numpy as np

print("\n===================================================")
print("  PROGRAM 2 : ReLU AND MAX POOLING")
print("===================================================\n")

# Task 1: Create Feature Map with positive and negative values
print("TASK 1 : INPUT FEATURE MAP")
print("---------------------------")

feature_map = [
    [ 3,  3,  3],
    [ 0,  0,  0],
    [-3, -3, -3]
]

feature_map = np.array(feature_map)
print("Feature Map:\n", feature_map)

# Task 2: Apply ReLU
print("\nTASK 2 : APPLY ReLU")
print("--------------------")
print("ReLU Rule:")
print("  If value <  0 → convert to 0")
print("  If value >= 0 → keep same")

relu_output = np.maximum(0, feature_map)

print("\nStep by Step:")
for i in range(len(feature_map)):
    for j in range(len(feature_map[0])):
        val = feature_map[i][j]
        out = relu_output[i][j]
        print(f"  ReLU({val}) = {out}")

print("\nReLU Output:\n", relu_output)

# Task 3: Apply 2x2 Max Pooling
print("\nTASK 3 : APPLY 2x2 MAX POOLING")
print("--------------------------------")
print("Max Pooling Rule:")
print("  Take maximum value from each 2x2 region")

pool_output = []

for i in range(0, len(relu_output) - 1, 2):
    row = []
    for j in range(0, len(relu_output[0]) - 1, 2):
        region = relu_output[i:i+2, j:j+2]
        max_val = np.max(region)
        print(f"\n  Region ({i},{j}):\n  {region}")
        print(f"  Max Value = {max_val}")
        row.append(max_val)
    pool_output.append(row)

pool_output = np.array(pool_output)

# Task 4: Display output after each step
print("\nTASK 4 : OUTPUT AFTER EACH STEP")
print("---------------------------------")
print("Input Feature Map:")
print(feature_map)
print("\nAfter ReLU:")
print(relu_output)
print("\nAfter Max Pooling:")
print(pool_output)

# Task 5: Explain why pooling reduces size
print("\nTASK 5 : WHY POOLING REDUCES SIZE")
print("------------------------------------")
print(f"  Input Size  : {feature_map.shape}")
print(f"  After ReLU  : {relu_output.shape}  (same size)")
print(f"  After Pool  : {pool_output.shape}  (reduced size)")
print("\nExplanation:")
print("  2x2 Max Pooling takes 4 values and gives 1 value")
print("  So every 2x2 block becomes 1 single value")
print("  This reduces the size by half in each direction")
print("  Less data = faster computation = less overfitting")