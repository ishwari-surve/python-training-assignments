import pandas as pd

Border = "-"*40
########################################################

#Step 1: Load the dataset 

#########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset:")
print(df.head())
print(df.tail())

print("Shape of dataset :",df.shape)
print("column Names :",list(df.columns))

print("\nData Types of Each Column:")
print(df.dtypes)