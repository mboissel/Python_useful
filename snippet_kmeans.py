import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Read the dataset from a tab-separated values (".tsv") file
file_path = 'path/to/your/file.tsv'
data = pd.read_csv(file_path, sep='\t')

# 2. Select the features for clustering (assuming all columns are features)
X = data.iloc[:, :]

# 3. Standardize the features (optional but often recommended for K-means)
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# 4. Perform K-means clustering
num_clusters = 3  # You can adjust the number of clusters based on your data
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(X_standardized)

# 5. Add the cluster labels to the original dataframe
data['Cluster'] = labels

# 6. Visualize the results (2D plot for simplicity, adapt as needed)
plt.scatter(X_standardized[:, 0], X_standardized[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, c='red', label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
