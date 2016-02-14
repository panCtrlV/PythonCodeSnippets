__author__ = 'panc'

import sys

# Read numbers from stdin and calculate the inverse
# for a given value

while True:
    # output to stdout:
    print "Yet another iteration ... (Ctrl-D to end)"
    try:
        # reading from sys.stdin (stop with Ctrl-D):
        num = raw_input("Enter a number: ")
        # print num
    except EOFError:
        print "\nNo more input. Bye!"
        break
    else:
        num = int(num)
        if num == 0:
            print >> sys.stderr, "\t0 has no inverse"
        else:
            print "\tinverse of %d is %f" % (num, 1./num)

# Execute by calling:
#
#   python streams_calinverse.py
#
# or provide a file "numbers.txt" with each line a number, then call
#
#   python streams_calinverse.py < numbers.txt