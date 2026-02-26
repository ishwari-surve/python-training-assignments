import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

Border = "--" * 40

#######################################################################
# Step 1: Decision Tree Visualization
#######################################################################

print(Border)
print("Step 4: Decision Tree Visualization")
print(Border)

plt.figure(figsize=(15,8))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree for Student Performance")

plt.show()
