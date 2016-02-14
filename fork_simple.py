__author__ = 'panc'


import os

# In this example, we fork a child process which
# call a function defined in the same script.
# That is, in the parent(), a child process is forked
# and it calls the child() function.

def child():
    print("\nA new child", os.getpid)
    os._exit(0)

def parent():
    # a parent process forks every time the
    # user types in a 'c', when prompted.
    while True:
        # fork and enter into a childe process
        newpid = os.fork()
        # 0 means we are in the child process
        # A positive number means we are in the
        # parent process.
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
        reply = raw_input("q for quit / c for new fork")
        if reply == 'c':
            continue
        else:
            break

parent()