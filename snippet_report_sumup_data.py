import pandas as pd
from pandas_profiling import ProfileReport

# Charger le jeu de données depuis un fichier (par exemple, CSV)
# Remplacez 'chemin/vers/votre/fichier.csv' par le chemin réel de votre fichier
file_path = 'chemin/vers/votre/fichier.csv'
data = pd.read_csv(file_path)

# Générer un rapport automatique
report = ProfileReport(data)

# Enregistrer le rapport au format HTML
report.to_file("rapport_aperçu.html")
