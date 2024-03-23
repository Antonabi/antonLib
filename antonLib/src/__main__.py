import os
import sys

def main():
    try:
        if sys.argv[1] == "-pd": #This is a debug function that prints the dir the __main__.py file is in. (I had problems with including the defAvatar.json)
            printDir()
    except:
        print("You found an easter egg! You can actually run antonLib.")
        
def printDir():
    print("This is a debug function that prints the dir the __main__.py file is in.")
    scriptPath = os.path.abspath(__file__)
    scriptDir = os.path.dirname(scriptPath)
    print(os.listdir(scriptDir))

__version__ = "0.1"

if __name__ == "__main__":
    main()
