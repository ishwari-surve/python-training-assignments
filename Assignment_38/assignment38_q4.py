#Question 4
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



print("Percentage of Passes and Failed students :",df["FinalResult"].value_counts(normalize=True)*100)

