import re
from typing import List, Dict, Tuple
from contentReader import CodeFile

def parse_code(file_content: List[str]) -> Tuple[List[List[str]], Dict[str, List[str]]]:
    execution_list = []  # Liste pour préparer l'exécution
    category_dict = {  # Dictionnaire pour le mappage des catégories
        "declarations": [],
        "objects": [],
        "methods": [],
        "strings": [],
        "variables": [],
        "lists": [],
        "operations": []
    }
    
    # Expression régulière pour identifier les éléments
    pattern = r'(\blet\b|\bconst\b)|(\w+)\.(\w+)|(\".*?\"|\'.*?\')|(\[.*?\])|(\w+)|(\=|\+|\-|\/|\*)'
    
    for line in file_content:
        line_elements = []  # Liste temporaire pour stocker les éléments de la ligne
        matches = re.findall(pattern, line)
        
        for match in matches:
            if match[0]:  # déclarations
                category_dict["declarations"].append(match[0])
                line_elements.append(match[0])
            elif match[1] and match[2]:  # objets et méthodes
                category_dict["objects"].append(match[1])
                category_dict["methods"].append(match[2])
                line_elements.extend([match[1], match[2]])
            elif match[3]:  # chaînes de caractères
                category_dict["strings"].append(match[3])
                line_elements.append(match[3])
            elif match[4]:  # listes
                category_dict["lists"].append(match[4])
                line_elements.append(match[4])
            elif match[5] and not match[1]:  # variables (en excluant les objets)
                category_dict["variables"].append(match[5])
                line_elements.append(match[5])
            elif match[6]:  # opérations
                category_dict["operations"].append(match[6])
                line_elements.append(match[6])
        
        execution_list.append(line_elements)
    
    return execution_list, category_dict

# Utilisation de la fonction parse_code sur le contenu de 'main.photon'
execution_order, categories = parse_code(CodeFile["main.photon"])
print(execution_order)
print(categories)
