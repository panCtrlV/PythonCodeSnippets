__author__ = 'panc'


import os

# It's possible to use execlpe() instead of execvpe(),
# demonstrated in "execvpe.py", but the code of our
# Python script has to be changed in the following way

path = os.environ['PATH'] + ":/Users/panc25/sandbox/pythonAdvancedTopics/monty/bin2"
env = {"PATH":path, "XYZ":"BlaBla"}
os.execlpe("test.sh", "test", "abc", env)
