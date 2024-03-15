# Fichier d'exécution pour le code Photon

from photonReader import parse_code, CodeFile  # Importation des fonctions et données nécessaires

class Console:
    @staticmethod
    def display(message):
        print(message)

    @staticmethod
    def color(color_name):
        # Cette méthode est un placeholder pour changer la couleur du texte.
        # L'implémentation dépendra de la façon dont vous souhaitez gérer les couleurs dans votre console.
        print(f"Changing text color to {color_name}")

# Utilisation de la fonction parse_code pour obtenir la liste d'exécution
execution_order, _ = parse_code(CodeFile["main.photon"])

# Boucle pour exécuter chaque instruction
for instruction in execution_order:
    if instruction[0] == "console":
        if instruction[1] == "display":
            Console.display(instruction[2].strip("'"))
        elif instruction[1] == "color":
            Console.color(instruction[2].strip("'"))
