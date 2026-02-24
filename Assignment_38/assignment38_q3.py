#Question 3 Using pandas functions, calculate and display
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

average_study_hours = df["StudyHours"].mean()
print("Average StudyHours:", average_study_hours)

average_attendance = df["Attendance"].mean()
print("Average Attendance:", average_attendance)

max_previous_score = df["PreviousScore"].max()
print("Maximum PreviousScore:", max_previous_score)

min_sleep_hours = df["SleepHours"].min()
print("Minimum SleepHours:", min_sleep_hours)