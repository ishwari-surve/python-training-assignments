#Question 7 Create a scatter plot of:
#StudyHours vs PreviousScore
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40
########################################################

#Step  

#########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.figure(figsize=(8,6))
sns.scatterplot(x="StudyHours",y="PreviousScore",data=df,color="Blue",s=100)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Hours Studied")
plt.ylabel("Previous Score")
plt.grid(True)

plt.show()