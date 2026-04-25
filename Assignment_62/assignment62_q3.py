import math

print("\n===================================================")
print("     PROGRAM 3 : FLATTENING")
print("===================================================\n")

# Task 1: Take a 2D Matrix
print("TASK 1 : INPUT 2D MATRIX")
print("-------------------------")

matrix = [
    [6, 4],
    [8, 6]
]

print("Matrix (2x2):")
for row in matrix:
    print(" ", row)

# Task 2: Convert 2D to 1D Vector
print("\nTASK 2 : CONVERT 2D TO 1D (FLATTEN)")
print("--------------------------------------")
print("Step by Step:")

flatten_output = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"  matrix[{i}][{j}] = {matrix[i][j]} → added to vector")
        flatten_output.append(matrix[i][j])

print(f"\nflatten_output = {flatten_output}")
print(f"Size before flatten : 2x2 = 4 values (2D)")
print(f"Size after  flatten : {len(flatten_output)} values (1D)")

# Task 3: Pass to Fully Connected Layer
print("\nTASK 3 : PASS TO FULLY CONNECTED LAYER")
print("----------------------------------------")

weights = [0.5, 0.3, 0.2, 0.4]
bias    = 0.1

print(f"Flatten Input : {flatten_output}")
print(f"Weights       : {weights}")
print(f"Bias          : {bias}")

# Task 4: Calculate Final Output Manually
print("\nTASK 4 : CALCULATE FINAL OUTPUT MANUALLY")
print("------------------------------------------")
print("Formula : z = (x1*w1) + (x2*w2) + (x3*w3) + (x4*w4) + bias")

weighted_sum = 0
print("\nStep by Step:")
for i in range(len(flatten_output)):
    val    = flatten_output[i]
    w      = weights[i]
    result = val * w
    weighted_sum += result
    print(f"  x{i+1}*w{i+1} = {val} * {w} = {result}")

weighted_sum += bias
print(f"\n  z = {weighted_sum - bias} + bias({bias}) = {weighted_sum}")

output = 1 / (1 + math.exp(-weighted_sum))
print(f"\n  Sigmoid(z) = 1 / (1 + e^(-{weighted_sum})) = {output:.4f}")

print(f"\nFinal Output : {output:.4f}")

if output >= 0.5:
    print("Decision     : Positive Class (1)")
else:
    print("Decision     : Negative Class (0)")

