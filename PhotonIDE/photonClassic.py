# Photon IDE developed by SkyDevelopment
from typing import *

from contentReader import CodeFile

def read_line(CodeLine : int):
    global CodeFile
    LINE : str = CodeFile[CodeLine]
    rest_of_line : str = LINE + "" # desinc of two variable
    columns : List[int] = []
    char : Tuple[int, str] = [-1,""] # [char index in line, char]
    while rest_of_line != "":
        char[0] += 1
        char[1] = rest_of_line[char[0]]
        if char[1] in [" "]:
            columns.append(rest_of_line[:char[1]])
            rest_of_line = rest_of_line[char[1]:]
            char = [-1, ""]


if __name__ == "__main__":
    print("""
  ___   _   _    ___   _____   ___    _   _
 | _ \ | |_| |  / _ \ |_   _| / _ \  | \ | |
 |  _/ |  _  | | |_| |  | |  | |_| | | |\| |
 |_|   |_| |_|  \___/   |_|   \___/  |_| \_| . py
 Developed by SkyDevelopement
=============================================================================
    """)
    # Finish of code with execution result
    print("""
=============================================================================
    """)
