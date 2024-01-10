# pip install pandas scikit-learn factor-analyzer

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Lire le jeu de données depuis un fichier Excel
nom_fichier_excel = 'chemin/vers/votre/fichier.xlsx'
donnees = pd.read_excel(nom_fichier_excel)

# 2. Ne garder que les données numériques
donnees_numeriques = donnees.select_dtypes(include=['number'])

# 3. Appliquer la normalisation de type "centré, réduit"
donnees_normalisees = StandardScaler().fit_transform(donnees_numeriques)

# 4. Appliquer une ACP sur le jeu de données normalisé
acp = PCA()
resultats_acp = acp.fit_transform(donnees_normalisees)

# Afficher les résultats de l'ACP
print("Charges factorielles :")
print(acp.components_)
print("\nVariance expliquée :")
print(acp.explained_variance_ratio_)
