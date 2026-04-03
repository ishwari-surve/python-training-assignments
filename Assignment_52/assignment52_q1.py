import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1: Load the Dataset

Border = '-'*40

df = pd.read_csv("student-mat.csv", sep=";")

print("Shape of Dataset:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())
print(Border)

# Step 2: Select Features and Preprocess


# Select only required features
features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
X = df[features]

print("Selected Features Shape:", X.shape)
print("\nNull Values:")
print(X.isnull().sum())

print("\nFeature Statistics:")
print(X.describe())

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nAfter Scaling:")
print(X_scaled[:5])

print(Border)

# Step 3: Find Best K using Elbow Method


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Curve
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method - Find Best K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

# Apply KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("Cluster Value Counts:")
print(df['Cluster'].value_counts())

print("\nFirst 5 Rows with Cluster:")
print(df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences', 'Cluster']].head())
print(Border)

# Step 4: Analyze and Visualize Clusters

# Show mean values of each cluster
print("Cluster Mean Values:")
print(df.groupby('Cluster')[features].mean())

# Label the clusters
df['Performance'] = df['Cluster'].map({
    0: 'Top Performers',
    1: 'Average Students',
    2: 'Struggling Students'
})

print("\nPerformance Group Count:")
print(df['Performance'].value_counts())

# Bar chart - Average G3 grade per cluster
df.groupby('Performance')['G3'].mean().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Average Final Grade (G3) per Cluster")
plt.xlabel("Performance Group")
plt.ylabel("Average G3 Grade")
plt.show()

# Scatter plot - G3 vs Absences
colors = {0: 'green', 1: 'orange', 2: 'red'}
for cluster in df['Cluster'].unique():
    subset = df[df['Cluster'] == cluster]
    plt.scatter(subset['G3'], subset['absences'],
                label=subset['Performance'].iloc[0],
                color=colors[cluster])

plt.title("Clusters - G3 vs Absences")
plt.xlabel("Final Grade G3")
plt.ylabel("Absences")
plt.legend()
plt.show()

# Boxplot - G3 grades per cluster
sns.boxplot(x='Performance', y='G3', data=df)
plt.title("G3 Grade Distribution per Cluster")
plt.xlabel("Performance Group")
plt.ylabel("Final Grade G3")
plt.show()
print(Border)