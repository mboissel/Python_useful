# pip install pandas seaborn scipy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# 1. Read the dataset from a CSV file
file_path = 'path/to/your/file.csv'
data = pd.read_csv(file_path, sep=',')

# 2. Create a heatmap with hierarchical clustering
# Using the seaborn library for simplicity
sns.set(font_scale=1)  # Adjust the font size as needed
g = sns.clustermap(data.corr(), method='average', cmap='coolwarm', annot=True, figsize=(10, 10))

# 3. Access the hierarchical clustering linkage matrix for rows and columns
row_linkage = g.dendrogram_row.linkage
col_linkage = g.dendrogram_col.linkage

# 4. Cut the dendrogram to obtain clusters (here, 3 clusters)
num_clusters = 3
row_clusters = fcluster(row_linkage, num_clusters, criterion='maxclust')
col_clusters = fcluster(col_linkage, num_clusters, criterion='maxclust')

# Print the cluster assignments for rows and columns
print("Row Clusters:", row_clusters)
print("Column Clusters:", col_clusters)

# Show the plot
plt.show()
