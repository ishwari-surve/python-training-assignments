import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousAdvertise(Datpath):
    Border = "-"*65
    ##########################################################
    # Step 1: Load Dataset
    ##########################################################
    
    print(Border)
    print("Step 1: Load Dataset")
    print(Border)
    df = pd.read_csv(Datpath)

    print("Few Records from Dataset: ")
    print(df.head())
    print(df.tail())

    ##########################################################
    # Step 2: Remove unwanted columns
    ##########################################################
    
    print(Border)
    print("Step 2: Remove unwanted columns")
    print(Border)

    print("Shape of Dataset Before the Removal: ",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Shape of Dataset After the Removal: ",df.shape)

    print(Border)
    print("Clean Dataset is: ")
    print(Border)

    print(df.head())
    print(df.tail())

    ##########################################################
    # Step 3: Check missing values
    ##########################################################
    
    print(Border)
    print("Step 3: Check missing values")
    print(Border)

    print("Missing Value count: \n",df.isnull().sum())

    ##########################################################
    # Step 4: Display Statstical Summary
    ##########################################################
    
    print(Border)
    print("Step 4: Display Statstical Summary")
    print(Border)

    print(df.describe())

    ##########################################################
    # Step 5: Corelation Betweeen Columns 
    ##########################################################
    
    print(Border)
    print("Step  5: Corelation Betweeen Columns ")
    print(Border)

    print("Corelation Matrix: ")
    print(df.corr())

    ################################################################
    # Step 6: Split Dataset into Dependent and Independent variables 
    ################################################################
    
    print(Border)
    print("Step  6: Split Dataset into Dependent and Independent variables  ")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independent variables:  ",X.shape)
    print("Shape of Dependent variables: ",Y.shape)

    ##########################################################
    # Step 7: Split the Dataset for Training and Testing
    ##########################################################
    
    print(Border)
    print("Step  7: Split the Dataset for Training and Testing ")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train Shape: ",X_train.shape)
    print("X_test Shape: ",X_test.shape)
    print("Y_train Shape: ",Y_train.shape)
    print("Y_test Shape: ",Y_test.shape)

    ##########################################################
    # Step 8: Create & train the Model
    ##########################################################
    
    print(Border)
    print("Step  8: Create & train the Model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    ##########################################################
    # Step 9: Test the Model
    ##########################################################
    
    print(Border)
    print("Step 9: Test the Model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)

    ##########################################################
    # Step 10: Evaluate the Model
    ##########################################################
    
    print(Border)
    print("Step 10: Evaluate the Model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Sqaure Error: ",MSE)
    print("Root Mean Sqaure error: ",RMSE)
    print("R_square value: ",R2)

    ##########################################################
    # Step 11: Calculate Model Coefficient
    ##########################################################
    
    print(Border)
    print("Step 11: Calculate Model Coefficient")
    print(Border)

    for column, value in zip(X.columns,model.coef_):
        print(f"{column} : {value}")
    
    print("Intercept value is: ",model.intercept_)

    ##########################################################
    # Step 12: Compare the Actual and Predicted Values
    ##########################################################
    
    print(Border)
    print("Step  12: Compare the Actual and Predicted Values")
    print(Border)

    Result = pd.DataFrame({
        'Actual Sale' : Y_test.values,
        'Predicted Sale ': Y_pred 
        })

    print(Result.head())

    ##########################################################
    # Step 13: Plot Actual vs Predicted
    ##########################################################
    
    print(Border)
    print("Step  13: Plot Actual vs Predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual Sales vs Predicted Sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()
