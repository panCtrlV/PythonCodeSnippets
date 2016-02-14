__author__ = 'panc'


import sys

# Demonstrate stdout redirect


# This is the regular stdout (no redirection)
print("Coming through regular stdout")

# stdout channel is saved
# `save_stdout` saves the original state of stdout
# so that it can be restored in the future
save_stdout = sys.stdout

# file where stdout is redirected
fh = open("test.txt", "w")
sys.stdout = fh
print("This line goes to test.txt")

# return to normal
sys.stdout = save_stdout

fh.close()
