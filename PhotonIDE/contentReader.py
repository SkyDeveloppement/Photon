# Photon IDE develloped by SkyDevellopement
import json

# Dictionnary for the storage of content of code file
CodeFile = {}

# Open the photon-pack.json file
with open("./photon-pack.json", "r") as pack:
    # Load JSON data
    data = json.load(pack)
    # Access the "code" attribute of JSON
    code_data = data.get("code", {})
    # Access the "file" attribute of "code"
    files = code_data.get("file", [])
    
    # Read the content of each specified file
    for file_name in files:
        with open(file_name, "r") as code_file:
            CodeFile[file_name] = code_file.read()