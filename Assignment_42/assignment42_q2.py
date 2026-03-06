#X = [1,2,3,4,5]
#Y = [3,4,2,4,5]

def MSE(actual_value,pred_value):
    if len(actual_value)!= len(pred_value):
        raise ValueError("Actual and Predicted values lists must have the same length")
    
    n = len(actual_value)
    total_square_error = 0

    for i in range(n):
        error = actual_value[i] - pred_value[i]
        total_square_error += error ** 2

    mse = total_square_error / n
    return mse

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

predicted_values = []

for i in X:
        y_pred = (slope * i) + c
        predicted_values.append(y_pred)
        print("For X =",i,"Predicted Y =",y_pred)

#Mean Squared Error (MSE)

mse_value = MSE(Y, predicted_values)
print(Border)
print("Mean Squared Error:", mse_value)
print(Border)

sum_value = 0

for i in predicted_values:
     value = i -  mean_y 
     sum_value = sum_value + value
     print("Y_pred - Y_bar",value)

print("Summation of Y_pred - Y_bar ** 2:" ,sum_value)
print(Border)

for i in predicted_values:
     value = (i -  mean_y) ** 2 
     sum_value = sum_value + value
     print("(Y_pred - Y_bar)**2",value)

print("(Summation of Y_pred - Y_bar) ** 2:" ,sum_value)
print(Border)

#R2 Score
R_sqrt = sum_value /sqrtX

print("R_square is:",R_sqrt)
print(Border)

     