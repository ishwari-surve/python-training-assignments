#Question 9
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

plt.figure(figsize=(8,6))
sns.regplot(
    data=df,
    x="AssignmentsCompleted",
    y="FinalResult",
    scatter_kws={'alpha':0.5,'color': 'blue'},
    line_kws={'color':'red'}
)

plt.title("Relationship between Assignment Completed and Final Result")
plt.xlabel("Number of Assignment Completed",fontsize=10)
plt.ylabel("Final Results",fontsize=10)

plt.show()
