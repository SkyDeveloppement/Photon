# Photon IDE developed by SkyDevelopment

from contentReader import CodeFile

class PhotonClassic:
    def __init__(self):
        self.variables = {}  # Dictionary to store variables and their types

    def execute_line(self, line):
        # Handling variable declarations
        if any(line.startswith(var_type) for var_type in ["const ", "let ", "var ", "secure "]):
            declaration, value = line.split(' = ')
            var_type, var_name = declaration.split()
            value = value.strip('";')

            # Handling value types
            if value.isdigit():
                value = int(value)  # Convert to number if it's a digit
            elif value in ["True", "False"]:
                value = value == "True"  # Convert to boolean if it's True or False
            # Add other type conversions if necessary

            # Store the variable with its type and value
            self.variables[var_name] = {"type": var_type, "value": value}

        # Handling console commands
        elif line.startswith("console.display"):
            tokens = line.split('console.display')
            content = tokens[1].strip("();\" ")
            
            # Check if content is a variable
            if content in self.variables:
                print(self.variables[content]["value"])  # Display the value of the variable
            else:
                print(content)  # Otherwise, print the content directly

    def execute_code(self):
        for file_name, lines in CodeFile.items():
            for line in lines:
                self.execute_line(line.strip())  # Call execute_line method for each line

if __name__ == "__main__":
    classic = PhotonClassic()  # Create an instance of the PhotonClassic class
    classic.execute_code()  # Call execute_code method on the instance
