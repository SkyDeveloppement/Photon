# Photon IDE développé par SkyDevelopment

from contentReader import CodeFile

class PhotonClassic:
    def __init__(self):
        self.variables = {}  # Dictionnaire pour stocker les variables et leurs types

    def execute_line(self, line):
        # Gestion des déclarations de variables
        if any(line.startswith(var_type) for var_type in ["const ", "let ", "var ", "secure "]):
            declaration, value = line.split(' = ')
            var_type, var_name = declaration.split()
            value = value.strip('";')

            # Gestion des types de valeur
            if value.isdigit():
                value = int(value)  # Convertir en nombre si c'est un chiffre
            elif value in ["True", "False"]:
                value = value == "True"  # Convertir en booléen si c'est True ou False
            # Ajouter d'autres conversions de type si nécessaire

            # Stocker la variable avec son type et sa valeur
            self.variables[var_name] = {"type": var_type, "value": value}

        # Gestion des commandes de la console
        elif line.startswith("console.display"):
            tokens = line.split('console.display')
            content = tokens[1].strip("();\" ")
            
            # Vérifier si le contenu est une variable
            if content in self.variables:
                print(self.variables[content]["value"])  # Afficher la valeur de la variable
            else:
                print(content)  # Sinon, afficher le contenu directement

    def execute_code(self):
        for file_name, lines in CodeFile.items():
            for line in lines:
                self.execute_line(line.strip())  # Appeler la méthode execute_line pour chaque ligne

if __name__ == "__main__":
    classic = PhotonClassic()  # Créer une instance de la classe PhotonClassic
    classic.execute_code()  # Appeler la méthode execute_code sur l'instance
