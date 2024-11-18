import csv

# Chemin vers le fichier CSV
csv_file_path = "my.csv"
output_file = "firewall/scripts/blocked_sites.txt"

# Liste pour stocker les URLs
urls = []

# Ouvrir et lire le fichier CSV
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Utiliser DictReader pour accéder aux colonnes par leur nom
    for row in reader:
        urls.append(row['url'])  # Récupérer uniquement la colonne 'url'

# Enregistrer les URLs
with open(output_file, mode='w', encoding='utf-8') as file_writter:
    for row in urls :
        file_writter.write(row + '\n')

