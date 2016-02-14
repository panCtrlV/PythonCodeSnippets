__author__ = 'panc'


# You should add ./monty/bin2 to PATH in command line before
# attempting to run this script, so that the test.sh script
# can be found on the PATH.

import os

args = ("test", "abc")
os.execvp("test.sh", args)