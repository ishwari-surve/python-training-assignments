import numpy as np

print("\n===================================================")
print("  PROGRAM 1 : MANUAL CONVOLUTION")
print("===================================================\n")

# Task 1: Input Image & Kernel
print("TASK 1 : LOAD INPUT")
print("----------------------")

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

image = np.array(image)
kernel = np.array(kernel)

print("Image:\n", image)
print("\nKernel:\n", kernel)

# Task 2: Perform Convolution
print("\nTASK 2 : PERFORM CONVOLUTION")
print("------------------------------")

output = []

for i in range(3):
    row = []
    for j in range(3):
        region = image[i:i+3, j:j+3]
        result = np.sum(region * kernel)

        print(f"\nRegion ({i},{j}):\n{region}")
        print("Calculation:", np.sum(region * kernel))
        
        row.append(result)
    output.append(row)

# Task 3: Feature Map
print("\nTASK 3 : FEATURE MAP")
print("----------------------")

feature_map = np.array(output)
print(feature_map)