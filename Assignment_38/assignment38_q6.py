#Question 6
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40
########################################################

#Step 1: Load the dataset 

#########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.figure(figsize=(8,5))

sns.histplot(df["StudyHours"],bins=10,kde=False,color="pink")
plt.show()

