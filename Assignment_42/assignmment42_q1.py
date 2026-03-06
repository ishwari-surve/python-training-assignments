#X = [1,2,3,4,5]
#Y = [3,4,2,4,5]

Border = "-"*40

print(Border)
print("Manual Simple Linear Regression ")
print(Border)

#Load the data
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

print("Dataset X:",X)
print("Dataset Y:",Y)


# Mean Calculation


mean_x̄ = sum(X)/n
mean_y = sum(Y)/n

print(Border)
print("Mean of X =",mean_x̄)
print("Mean of Y =",mean_y)


# Slope Calculation

devationX = [i - mean_x̄ for i in X]
devationY = [i - mean_y for i in Y]

print("X - X_bar:", devationX)
print("Y - Y_bar:", devationY)
print(Border)

product_of_deviation = []

for X_i, Y_i in zip(X, Y):
    devationX = X_i - mean_x̄
    devationY = Y_i - mean_y
    product = devationX * devationY
    product_of_deviation.append(product)

print("Product of Deviation:", product_of_deviation)

sum_product = sum(product_of_deviation)

print("Sum of (X - X_bar) * (Y - Y_bar):", sum_product)
print(Border)

sqrtX = 0

for i in X:
    square = (i - mean_x̄) ** 2
    sqrtX = sqrtX + square

print("Sum of (X - X_bar)^2 :", sqrtX)

sum_squareY = 0

for i in Y:
    square = (i - mean_y) ** 2
    sum_squareY = sum_squareY + square

print("Sum of (Y - Y_bar)^2 :", sum_squareY)

slope = sum_product/sqrtX
print("Slope is:",slope)
print(Border)

# Intercept

c = -(slope) * mean_x̄ + mean_y

print("Intercept (c):", c)

print(Border)

# Regression Equation


print(Border)
print("Regression Equation")
print("Y =",slope,"X +",c)


# Prediction


x_new = 6

y_pred = slope*x_new + c

print(Border)
print("Predicted Y for X=6 :",y_pred)
print(Border)