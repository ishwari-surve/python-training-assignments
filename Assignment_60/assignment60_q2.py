import math
import matplotlib.pyplot as plt

print("\n===================================================")
print("  PROGRAM 2 : ACTIVATION FUNCTIONS DEMO")
print("===================================================\n")

# Step 1: Input values from -10 to 10
x_values = list(range(-10, 11))

print("STEP 1 : INPUT VALUES (-10 to 10)")
print("-----------------------------------")
print(f"  x values = {x_values}")

# Step 2: Define Activation Functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def tanh(x):
    return math.tanh(x)

sigmoid_values = [sigmoid(x) for x in x_values]
relu_values    = [relu(x)    for x in x_values]
tanh_values    = [tanh(x)    for x in x_values]

print("\nSTEP 2 : ACTIVATION FUNCTION VALUES")
print("--------------------------------------")
print("\nSigmoid Values:")
for x, y in zip(x_values, sigmoid_values):
    print(f"  sigmoid({x:3}) = {y:.4f}")

print("\nReLU Values:")
for x, y in zip(x_values, relu_values):
    print(f"  relu({x:3}) = {y}")

print("\nTanh Values:")
for x, y in zip(x_values, tanh_values):
    print(f"  tanh({x:3}) = {y:.4f}")

# Step 3: Plot all activation functions
print("\nSTEP 3 : PLOTTING ALL ACTIVATION FUNCTIONS")
print("--------------------------------------------")

plt.plot(x_values, sigmoid_values, label="Sigmoid", color="blue",  marker="o")
plt.plot(x_values, relu_values,    label="ReLU",    color="green", marker="s")
plt.plot(x_values, tanh_values,    label="Tanh",    color="red",   marker="^")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Activation Functions: Sigmoid, ReLU, Tanh")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Explain each activation function
print("\nSTEP 4 : EXPLANATION")
print("----------------------")
print("Sigmoid:")
print("  Formula  : 1 / (1 + e^-x)")
print("  Range    : 0 to 1")
print("  Used for : Output layer in binary classification")

print("\nReLU:")
print("  Formula  : max(0, x)")
print("  Range    : 0 to infinity")
print("  Used for : Hidden layers in deep networks")

print("\nTanh:")
print("  Formula  : (e^x - e^-x) / (e^x + e^-x)")
print("  Range    : -1 to 1")
print("  Used for : Hidden layers, better than sigmoid")