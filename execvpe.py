__author__ = 'panc'

import os

# Using os.execvpe allows a third arguement env (
# takes a dictionary as the value) which specifies
# environment variables.
#
# If environment variables already exist, e.g. PATH,
# they will be replaced by the corresponding values
# of the dictionary. If an environment does not exist,
# e.g. XYZ, it will be created.
#
# So the user can avoid append the directory to the
# PATH, as what we did in "fork_execvp.py".

path = os.environ['PATH'] + ":/Users/panc25/sandbox/pythonAdvancedTopics/monty/bin2"
env = {"PATH":path, "XYZ":"BlaBla"}
args = ("test", "abc")
os.execvpe("test.sh", args, env)
