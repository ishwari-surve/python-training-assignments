#Final Code
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

########################################################

#Step  2: Load Dataset and Displaying

########################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset:")
print(df.head())
print(df.tail())

print("Shape of dataset :",df.shape)
print("column Names :",list(df.columns))

print("\nData Types of Each Column:")
print(df.dtypes)

########################################################

#Step  3: Analyzing of Data

#########################################################
print(Border)


total_students = df.shape[0]
print("Total Students:", total_students)

passed_students = df[df["FinalResult"] == 1].shape[0]
print("Passed Students:", passed_students)

failed_students = df[df["FinalResult"] == 0].shape[0]
print("Failed Students:", failed_students)

########################################################

#Step  4: Calculating percentage of Pass fail

#########################################################

print("Percentage of Passes and Failed students :",df["FinalResult"].value_counts(normalize=True)*100)

#######################################################################
# Step 5: Plotting Histogram
#######################################################################

plt.figure(figsize=(8,5))

sns.histplot(df["StudyHours"],bins=10,kde=False,color="pink")
plt.show()

#######################################################################
# Step 6: Scatter Plot
#######################################################################

plt.figure(figsize=(8,6))
sns.scatterplot(x="StudyHours",y="PreviousScore",data=df,color="Blue",s=100)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Hours Studied")
plt.ylabel("Previous Score")
plt.grid(True)

plt.show()

#######################################################################
# Step 7: Box Plot
#######################################################################

sns.boxplot(data=df,x="Attendance")
plt.title("Students Performance ML")
plt.show()

#######################################################################
# Step 8: Relationship between Assignment Completed and Final Result
#######################################################################

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

#######################################################################
# Step 9: Relationship between Sleep Hours and Final Result
#######################################################################

plt.figure()
sns.boxplot(x="FinalResult", y="SleepHours", data=df)


plt.title("SleepHours vs FinalResult")
plt.xlabel("FinalResult (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")


plt.show()

