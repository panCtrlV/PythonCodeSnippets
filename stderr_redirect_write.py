__author__ = 'panc'


import sys


# You can also write to stderr directly,
# instead of just redirecting the errors
# from python runtime.
# This can be achieved by appending `>> sys.stderr`
# to a print statement.


save_stderr = sys.stderr

fh = open("errors.txt", "w")
sys.stderr = fh

print >> sys.stderr, "printing to errors.txt"

# return to normal
sys.stderr = save_stderr

fh.close()
