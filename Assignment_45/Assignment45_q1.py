import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    Border = "-"*40

#######################################################################
# Step 1: Load the Dataset
#######################################################################
    
    print(Border)
    print("Step 1: Load the Dataset")
    print(Border)

    df = pd.read_csv(Datapath)
    print(Border)
    print("Some Entries from Dataset")
    print(df.head())
    print(Border)

#######################################################################
# Step 2: Clean the Dataset by removing Empty Rows
#######################################################################
    
    print(Border)
    print("Step 2: Clean the Dataset by removing Empty Rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total Records: ",df.shape[0])
    print("Total Columns: ",df.shape[1])
    print(Border)

#######################################################################
# Step 3: Seperate Independent and Dependent Variable 
#######################################################################
    
    print(Border)
    print("Step 3: Seperate Independent and Dependent Variable ")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']
    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)
    print(Border)

    print("Input Columns: ",X.columns.tolist())
    print("Output Columns: Class ")

#######################################################################
# Step 4: Split the Dataset for Training and Testing
#######################################################################
    
    print(Border)
    print("Step 4: Split the Dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    
    print(Border)
    print("Information of Training and Testing Data")
    print("X_train: ",X_train.shape)
    print("X_test: ",X_test.shape)
    print("Y_train: ",Y_train.shape)
    print("Y_test: ",Y_test.shape)

#######################################################################
# Step 5: Features Scaling
#######################################################################
    
    print(Border)
    print("Step 5: Features Scaling")
    print(Border)

    scaler = StandardScaler()
    # Independent Variable Scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    print("Features Scaling is done!!!!!")

#######################################################################
# Step 6: Explore the Multiple Values of K
#######################################################################
    # Hyperparameter Tuning (K)

    print(Border)
    print("Step 6: Explore the Multiple Values of K")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy Report on K values(1 to 20)")
    
    for value in accuracy_scores:
        print(value)
    print(Border)

#######################################################################
# Step 7: Plot graph of K vs Accuracy
########################################################################

    print(Border)
    print("Step 7: Plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores, marker = 'o')
    plt.title("K value vs Accuracy")
    plt.xlabel("Values of k")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(K_values)
    plt.show()  
    
#######################################################################
# Step 8: Find Best Value of K
########################################################################
    
    print(Border)
    print("Step 8: Find Best Value of K")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of K is: ",best_k)    #K=9

#######################################################################
# Step 9: Build Final Model usinf the Best value of K
########################################################################
    
    print(Border)
    print("Step 9: Build Final Model usinf the Best value of K")
    print(Border)

    Final_model = KNeighborsClassifier(n_neighbors= best_k)
    Final_model.fit(X_train_scaled,Y_train)
    Y_pred = Final_model.predict(X_test_scaled)

#######################################################################
# Step 10: Calculate Final Accuracy
########################################################################
    
    print(Border)
    print("Step 10: Calculate Final Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of Model is: ",accuracy*100)

#######################################################################
# Step 11: Display Confusion Matrix
########################################################################
    
    print(Border)
    print("Step 11: Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

#######################################################################
# Step 12: Display Classififciation Report
########################################################################
    
    print(Border)
    print("Step 12: Display Classififciation Report")
    print(Border)

    print(classification_report(Y_test,Y_pred))
    
def main():
    Border = "-"*60
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":

    main()
