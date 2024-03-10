# Photon IDE developed by SkyDevelopment

from contentReader import CodeFile

class PhotonClassic:
    def __init__(self):
        self.variables = {}  # Dictionary to store variables

    def execute_line(self, line):
        # Split line into tokens based on the console.display command
        if line.startswith("console.display"):
            tokens = [line[:line.find("(")], line[line.find("(")+1:line.find(")")]]
        else:
            tokens = line.split()

        if tokens[0] == "console.display":
            # Console display: console.display("message")
            if len(tokens) == 2 and tokens[1].startswith('"') and tokens[1].endswith('"'):
                message = tokens[1][1:-1]  # Extract message from tokens (removing quotes)
                print(message)  # Print the message
            else:
                print("54")
                print("Error: Invalid format for console.display statement")
        # Add more execution logic for other types of statements (e.g., conditions, loops)



if __name__ == "__main__":
    classic = PhotonClassic()  # Create an instance of the PhotonClassic class
    for file_name, code in CodeFile.items():
        print(f"Executing code from {file_name}:")
        classic.execute_line(code)  # Call execute_code method on the instance
