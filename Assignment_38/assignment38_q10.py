#Question 10
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

plt.figure()
sns.boxplot(x="FinalResult", y="SleepHours", data=df)


plt.title("SleepHours vs FinalResult")
plt.xlabel("FinalResult (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")


plt.show()