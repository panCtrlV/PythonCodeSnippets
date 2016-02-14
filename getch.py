__author__ = 'panc'

import os, platform

# Read a character without having to type the return key


my_platform = platform.system()

if my_platform == "Windows":
    import msvcrt

def getch():
    if my_platform in ["Linux", "Darwin"]:
        os.system("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()

print("Type one character!")
getch()
print("\nOkay")
