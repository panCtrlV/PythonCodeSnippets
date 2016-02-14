__author__ = 'panc'


import os

# Python can accept any shell commands and execute.
# The output of the shell script can be captured.
# In this example, the output from execution of the
# shell command is read line by line and processed
# by Python.

command = " "
while command != "exit":
    command = raw_input("Command: ")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print line
    handle.close()

print "That's it. Bye!"
