# Question 2
import pandas as pd
import numpy as np

Border = "-"*40
########################################################

#Step 1: Load the dataset 

#########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

total_students = df.shape[0]
print("Total Students:", total_students)

passed_students = df[df["FinalResult"] == 1].shape[0]
print("Passed Students:", passed_students)

failed_students = df[df["FinalResult"] == 0].shape[0]
print("Failed Students:", failed_students)