#Question 8 Boxplot for Attendance.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40
########################################################

#Step  1: Load Dataset

#########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

sns.boxplot(data=df,x="Attendance")
plt.title("Students Performance ML")
plt.show()