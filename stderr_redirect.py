__author__ = 'panc'

import sys

# Demonstrate stderr redirect
# Save python errors in a file
# instead of print it in the terminal


# save the current state of stderr
save_stderr = sys.stderr

# redirect error
fh = open("errors.txt", 'w')
sys.stderr = fh

x = 10/0

# return to normal
sys.stderr = save_stderr

fh.close()