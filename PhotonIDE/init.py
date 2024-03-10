import json

def init_photon_pack():
    # Structure de base pour photon-pack.json
    base_structure = {
        "code": {
            "file": ["main.photon"],
            "version": "1.0.0",
            "console": True,
            "app": False,
            "web": False,
            "subprocess": False
        },
        "IDE": {
            "version": "1.0.0",
            "ID": "Alpha",
            "kit": "Devkit6 - 1.0.0"
        },
        "Library": {
            "network": "1.0.0",
            "machine": "1.0.0",
            "os": "1.0.0",
            "boson": "1.0.0",
            "webkit": "1.0.0",
            "atom": "1.0.0"
        },
        "Import": ["script.js", "type.ts"],
        "Database": {
            "used": "sqlite",
            "db": ["db.sqlite"]
        }
    }

    # Écrire la structure de base dans le fichier photon-pack.json
    with open('photon-pack.json', 'w') as file:
        json.dump(base_structure, file, indent=4)

# Appeler la fonction pour initialiser le fichier
init_photon_pack()
