import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Border = "-" * 40

########################################################
# Step 1 : Get Data
########################################################

print(Border)
print("Step 1 : Load Dataset")
print(Border)

DatasetPath = "PlayPredictor.csv"

df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully")
print(df)

########################################################
# Step 2 : Clean, Prepare and Manipulate Data
########################################################

print(Border)
print("Step 2 : Label Encoding")
print(Border)

Weather_encoder = LabelEncoder()
Temp_encoder = LabelEncoder()
Play_encoder = LabelEncoder()

df['Whether'] = Weather_encoder.fit_transform(df['Whether'])
df['Temperature'] = Temp_encoder.fit_transform(df['Temperature'])
df['Play'] = Play_encoder.fit_transform(df['Play'])

print("Encoded Dataset")
print(df)

########################################################
# Step 3 : Train Data
########################################################

print(Border)
print("Step 3 : Train Model")
print(Border)

X = df[['Whether','Temperature']]
Y = df['Play']

model = KNeighborsClassifier(n_neighbors = 3)

model.fit(X,Y)

print("Model trained successfully")

########################################################
# Step 4 : Test Data
########################################################

print(Border)
print("Step 4 : Test Data")
print(Border)

New_data = [[0,2]]

Prediction = model.predict(New_data)

if Prediction[0] == 1:
    print("Prediction : Yes")
else:
    print("Prediction : No")

########################################################
# Step 5 : Calculate Accuracy
########################################################

def CheckAccuracy():

    print(Border)
    print("Step 5 : Check Accuracy")
    print(Border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size = 0.5,
        random_state = 42
    )

    for k in range(1,6):

        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test,Y_pred)

        print("K =",k,"Accuracy :",acc*100)



if __name__ == "__main__":
    CheckAccuracy()