# Photon IDE develloped by SkyDevellopement
import json

# Dictionnaire pour le stockage du contenu des fichiers de code
CodeFile = {}

# Ouvrir le fichier photon-pack.json
with open("./photon-pack.json", "r") as pack:
    # Charger les données JSON
    data = json.load(pack)
    # Accéder à l'attribut "code" de JSON
    code_data = data.get("code", {})
    # Accéder à l'attribut "file" de "code"
    files = code_data.get("file", [])
    
    # Lire le contenu de chaque fichier spécifié
    for file_name in files:
        with open(file_name) as reader:
            # Vérifier si la clé existe dans TempCodeFile, sinon créer une liste vide
            if file_name not in CodeFile:
                CodeFile[file_name] = []
            # Lire chaque ligne du fichier et l'ajouter à la liste correspondante
            for line in reader:
                CodeFile[file_name].append(line)
