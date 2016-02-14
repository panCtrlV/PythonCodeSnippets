__author__ = 'panc'


import sys

# Accepting command line arguments passed to a
# python script

print "It's easy to print this list of course: ",
print sys.argv

print "or it can be iterated via a for loop: "
for i in range(len(sys.argv)):
    if i == 0:
        print "Script name: %s" % sys.argv[0]
    else:
        print "\t%d. argument: %s" % (i,sys.argv[i])

# call in command line as: python commandline_args.py arg1 arg2

